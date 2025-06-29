from flask import Flask, render_template, request, send_file
import math
import matplotlib.pyplot as plt
import os
import csv

app = Flask(__name__)
last_result = {}

def calculate_power(voltage, current, pf, phase):
    if phase == "single":
        real_power = voltage * current * pf
        apparent_power = voltage * current
    else:  # three
        real_power = math.sqrt(3) * voltage * current * pf
        apparent_power = math.sqrt(3) * voltage * current

    reactive_power = math.sqrt(abs(apparent_power**2 - real_power**2))

    return {
        "P (kW)": real_power / 1000,
        "Q (kVAR)": reactive_power / 1000,
        "S (kVA)": apparent_power / 1000
    }

def plot_triangle(P, Q):
    plt.figure(figsize=(6, 4))
    plt.plot([0, P], [0, 0], label="P (Real)", color="green", linewidth=2)
    plt.plot([P, P], [0, Q], label="Q (Reactive)", color="blue", linewidth=2)
    plt.plot([0, P], [0, Q], label="S (Apparent)", color="red", linestyle="--", linewidth=2)

    plt.title("Power Triangle")
    plt.xlabel("kW")
    plt.ylabel("kVAR")
    plt.grid(True)
    plt.axis("equal")
    plt.legend()
    plt.tight_layout()
    plt.savefig("static/power_triangle.png")
    plt.close()

@app.route("/", methods=["GET", "POST"])
def index():
    global last_result
    result = None

    if request.method == "POST":
        try:
            voltage = float(request.form["voltage"])
            current = float(request.form["current"])
            pf = float(request.form["pf"])
            phase = request.form["phase"]

            result = calculate_power(voltage, current, pf, phase)
            result.update({
                "Voltage": voltage,
                "Current": current,
                "Power Factor": pf,
                "Phase": phase.capitalize()
            })

            last_result = result

            plot_triangle(result["P (kW)"], result["Q (kVAR)"])

        except Exception as e:
            result = {"error": str(e)}

    return render_template("index.html", result=result)

@app.route("/export")
def export():
    if not last_result:
        return "No data to export."

    file_path = "static/power_result.csv"
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(last_result.keys())
        writer.writerow(last_result.values())
    return send_file(file_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
