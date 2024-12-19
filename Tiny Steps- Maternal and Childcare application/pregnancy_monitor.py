import tkinter as tk
from tkinter import ttk, messagebox

def save_data():
    try:
        weekly_checkup_date = entry_date.get()
        weight = float(entry_weight.get())
        blood_pressure = entry_blood_pressure.get()
        blood_sugar_levels = entry_blood_sugar.get()
        medication_taken = entry_medication.get()
        energy_level = energy_level_var.get()
        mood_swing = mood_swing_var.get()
        body_changes = [var.get() for var in body_change_vars if var.get()]
        avg_calories_burnt = float(entry_calories.get())

        data = f"Weekly Checkup Date: {weekly_checkup_date}\nWeight: {weight}\nBlood Pressure: {blood_pressure}\nBlood Sugar Levels: {blood_sugar_levels}\nMedication Taken: {medication_taken}\nEnergy Level: {energy_level}\nMood Swing: {mood_swing}\nBody Changes: {', '.join(body_changes)}\nAverage Calories Burnt: {avg_calories_burnt}"
        messagebox.showinfo("Saved Data", data)
    except ValueError as e:
        messagebox.showerror("Error", "Invalid input. Please check your entries and try again.")
    except Exception as e:
        messagebox.showerror("Error", f"Error saving data: {e}")

root = tk.Tk()
root.title("Pregnancy Monitoring System")

# Create a frame for the form
form_frame = ttk.Frame(root, padding="20")
form_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

# Weekly Checkup Date
tk.Label(form_frame, text="Weekly Checkup Date (DD/MM/YYYY):").grid(row=0, column=0, sticky=tk.W)
entry_date = tk.Entry(form_frame)
entry_date.grid(row=0, column=1)

# Weight
tk.Label(form_frame, text="Weight (kg):").grid(row=1, column=0, sticky=tk.W)
entry_weight = tk.Entry(form_frame)
entry_weight.grid(row=1, column=1)

# Blood Pressure
tk.Label(form_frame, text="Blood Pressure:").grid(row=2, column=0, sticky=tk.W)
entry_blood_pressure = tk.Entry(form_frame)
entry_blood_pressure.grid(row=2, column=1)

# Blood Sugar Levels
tk.Label(form_frame, text="Blood Sugar Levels:").grid(row=3, column=0, sticky=tk.W)
entry_blood_sugar = tk.Entry(form_frame)
entry_blood_sugar.grid(row=3, column=1)

# Medication Taken
tk.Label(form_frame, text="Medication Taken:").grid(row=4, column=0, sticky=tk.W)
entry_medication = tk.Entry(form_frame)
entry_medication.grid(row=4, column=1)

# Energy Levels
tk.Label(form_frame, text="Energy Levels:").grid(row=5, column=0, sticky=tk.W)
energy_level_var = tk.StringVar()
tk.Radiobutton(form_frame, text="Low", variable=energy_level_var, value="Low").grid(row=5, column=1, sticky=tk.W)
tk.Radiobutton(form_frame, text="Intermediate", variable=energy_level_var, value="Intermediate").grid(row=5, column=2, sticky=tk.W)
tk.Radiobutton(form_frame, text="High", variable=energy_level_var, value="High").grid(row=5, column=3, sticky=tk.W)

# Mood Swings
tk.Label(form_frame, text="Mood Swings:").grid(row=6, column=0, sticky=tk.W)
mood_swing_var = tk.StringVar()
tk.Radiobutton(form_frame, text="Low", variable=mood_swing_var, value="Low").grid(row=6, column=1, sticky=tk.W)
tk.Radiobutton(form_frame, text="Intermediate", variable=mood_swing_var, value="Intermediate").grid(row=6, column=2, sticky=tk.W)
tk.Radiobutton(form_frame, text="High", variable=mood_swing_var, value="High").grid(row=6, column=3, sticky=tk.W)

# Body Changes
tk.Label(form_frame, text="Body Changes:").grid(row=7, column=0, sticky=tk.W)
body_change_vars = []
body_changes = [
    "Breast changes", "Constipation", "Dizziness", "Fatigue, sleep problems",
    "Heartburn and indigestion", "Hemorrhoids", "Itching", "Leg cramps",
    "Morning sickness", "Nasal problems", "Numb or tingling hands",
    "Stretch marks", "Swelling", "Urinary frequency"
]
for idx, change in enumerate(body_changes, start=7):
    var = tk.StringVar()
    body_change_vars.append(var)
    tk.Checkbutton(form_frame, text=change, variable=var, onvalue=change, offvalue="").grid(row=idx, column=1, sticky=tk.W)

# Average Calories Burnt
tk.Label(form_frame, text="Average Calories Burnt per Day:").grid(row=22, column=0, sticky=tk.W)
entry_calories = tk.Entry(form_frame)
entry_calories.grid(row=22, column=1)

# Save Button
save_button = tk.Button(root, text="Save", command=save_data)
save_button.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

root.mainloop()