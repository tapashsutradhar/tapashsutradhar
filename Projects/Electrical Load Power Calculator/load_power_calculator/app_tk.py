import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import math
import csv
import matplotlib.pyplot as plt

def calculate_power():
    try:
        voltage = float(entry_voltage.get())
        current = float(entry_current.get())
        pf = float(entry_pf.get())
        phase = phase_type.get()

        if not (0 <= pf <= 1):
            raise ValueError("Power Factor must be between 0 and 1.")

        if phase == "Single-phase":
            real_power = voltage * current * pf
            apparent_power = voltage * current
        else:  # Three-phase
            real_power = math.sqrt(3) * voltage * current * pf
            apparent_power = math.sqrt(3) * voltage * current

        reactive_power = math.sqrt(abs(apparent_power**2 - real_power**2))

        label_result.config(
            text=f"Real Power (P): {real_power/1000:.2f} kW\n"
                 f"Reactive Power (Q): {reactive_power/1000:.2f} kVAR\n"
                 f"Apparent Power (S): {apparent_power/1000:.2f} kVA"
        )

        # Store for export/plotting
        global last_result
        last_result = {
            "Voltage": voltage,
            "Current": current,
            "Power Factor": pf,
            "Phase": phase,
            "P (kW)": real_power / 1000,
            "Q (kVAR)": reactive_power / 1000,
            "S (kVA)": apparent_power / 1000
        }

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

def export_to_csv():
    if not last_result:
        messagebox.showwarning("No data", "Calculate results before exporting.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                             filetypes=[("CSV files", "*.csv")])
    if file_path:
        with open(file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(last_result.keys())
            writer.writerow(last_result.values())
        messagebox.showinfo("Exported", f"Data saved to:\n{file_path}")

def plot_power_triangle():
    if not last_result:
        messagebox.showwarning("No data", "Calculate results before plotting.")
        return

    P = last_result["P (kW)"]
    Q = last_result["Q (kVAR)"]
    S = last_result["S (kVA)"]

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
    plt.show()

# GUI setup
root = tk.Tk()
root.title("Advanced Load Power Calculator")
root.geometry("450x420")
root.resizable(False, False)

tk.Label(root, text="Electrical Load Power Calculator", font=("Arial", 14, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=5)

# Inputs
tk.Label(frame, text="Phase Type:").grid(row=0, column=0, sticky='e')
phase_type = ttk.Combobox(frame, values=["Single-phase", "Three-phase"], state="readonly")
phase_type.grid(row=0, column=1, padx=10)
phase_type.current(0)

tk.Label(frame, text="Voltage (V):").grid(row=1, column=0, sticky='e')
entry_voltage = tk.Entry(frame)
entry_voltage.grid(row=1, column=1)

tk.Label(frame, text="Current (A):").grid(row=2, column=0, sticky='e')
entry_current = tk.Entry(frame)
entry_current.grid(row=2, column=1)

tk.Label(frame, text="Power Factor:").grid(row=3, column=0, sticky='e')
entry_pf = tk.Entry(frame)
entry_pf.grid(row=3, column=1)

# Buttons
tk.Button(root, text="Calculate", command=calculate_power, bg="#4CAF50", fg="white", width=18).pack(pady=10)
label_result = tk.Label(root, text="", font=("Arial", 11), justify="left")
label_result.pack()

tk.Button(root, text="Export to CSV", command=export_to_csv, bg="#2196F3", fg="white", width=18).pack(pady=5)
tk.Button(root, text="Show Power Triangle", command=plot_power_triangle, bg="#FF5722", fg="white", width=18).pack(pady=5)

# Store last result for exporting
last_result = {}

# Run GUI
root.mainloop()
