from flask import Flask, render_template, request, redirect, session, url_for, send_file
from models import db, User, Calculation
import os, math, matplotlib.pyplot as plt
import csv

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.secret_key = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize extensions
    db.init_app(app)
    
    # Register routes
    @app.route("/", methods=["GET", "POST"])
    def index():
        if "user_id" not in session:
            return redirect("/login")

        result = None
        if request.method == "POST":
            try:
                voltage = float(request.form["voltage"])
                current = float(request.form["current"])
                pf = float(request.form["pf"])
                phase = request.form["phase"]

                P, Q, S = calculate_power(voltage, current, pf, phase)
                plot_triangle(P, Q)

                # Save to DB
                calc = Calculation(
                    voltage=voltage, current=current, pf=pf, phase=phase,
                    real_power=P, reactive_power=Q, apparent_power=S,
                    user_id=session["user_id"]
                )
                db.session.add(calc)
                db.session.commit()

                result = {"P": P, "Q": Q, "S": S}
            except Exception as e:
                result = {"error": str(e)}

        return render_template("index.html", result=result)

    @app.route("/register", methods=["GET", "POST"])
    def register():
        if request.method == "POST":
            username = request.form["username"]
            password = request.form["password"]
            if User.query.filter_by(username=username).first():
                return "Username already exists."
            user = User(username=username)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            return redirect("/login")
        return render_template("register.html")

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            username = request.form["username"]
            password = request.form["password"]
            user = User.query.filter_by(username=username).first()
            if user and user.check_password(password):
                session["user_id"] = user.id
                return redirect("/")
            else:
                return "Invalid credentials"
        return render_template("login.html")

    @app.route("/logout")
    def logout():
        session.clear()
        return redirect("/login")

    @app.route("/history")
    def history():
        if "user_id" not in session:
            return redirect("/login")
        user_calcs = Calculation.query.filter_by(user_id=session["user_id"]).all()
        return render_template("history.html", calcs=user_calcs)

    @app.route("/export")
    def export():
        if "user_id" not in session:
            return redirect("/login")
        calcs = Calculation.query.filter_by(user_id=session["user_id"]).all()
        file_path = "static/history.csv"
        with open(file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Voltage", "Current", "Power Factor", "Phase", "P (kW)", "Q (kVAR)", "S (kVA)"])
            for c in calcs:
                writer.writerow([c.voltage, c.current, c.pf, c.phase, c.real_power, c.reactive_power, c.apparent_power])
        return send_file(file_path, as_attachment=True)

    # Create database tables
    with app.app_context():
        db.create_all()

    return app

# Helper functions (not route-dependent)
def calculate_power(voltage, current, pf, phase):
    if phase == "single":
        P = voltage * current * pf
        S = voltage * current
    else:
        P = math.sqrt(3) * voltage * current * pf
        S = math.sqrt(3) * voltage * current
    Q = math.sqrt(abs(S**2 - P**2))
    return round(P/1000, 2), round(Q/1000, 2), round(S/1000, 2)

def plot_triangle(P, Q):
    plt.figure(figsize=(5, 4))
    plt.plot([0, P], [0, 0], label="P (Real)", color="green")
    plt.plot([P, P], [0, Q], label="Q (Reactive)", color="blue")
    plt.plot([0, P], [0, Q], label="S (Apparent)", color="red", linestyle="--")
    plt.title("Power Triangle")
    plt.grid(True)
    plt.axis("equal")
    plt.legend()
    plt.tight_layout()
    plt.savefig("static/power_triangle.png")
    plt.close()

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)