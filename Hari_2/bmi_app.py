import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from datetime import datetime
import os


class BMIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator & History")
        self.root.geometry("700x600")
        self.root.resizable(False, False)

        # Set color scheme
        self.bg_color = "#000000"
        self.primary_color = "#4CAF50"
        self.secondary_color = "#2196F3"

        self.root.configure(bg=self.bg_color)

        # File path for storing data
        self.data_file = "bmi_data.txt"

        self.create_widgets()
        self.load_history()

    def create_widgets(self):
        # Title
        title_frame = tk.Frame(self.root, bg=self.primary_color, height=60)
        title_frame.pack(fill=tk.X)
        title_frame.pack_propagate(False)

        title_label = tk.Label(
            title_frame,
            text="BMI Calculator",
            font=("Arial", 24, "bold"),
            bg=self.primary_color,
            fg="white",
        )
        title_label.pack(pady=10)

        # Main container
        main_frame = tk.Frame(self.root, bg=self.bg_color)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Input Section
        input_frame = tk.LabelFrame(
            main_frame,
            text="Input Data",
            font=("Arial", 12, "bold"),
            bg=self.bg_color,
            padx=20,
            pady=15,
        )
        input_frame.pack(fill=tk.X, pady=(0, 20))

        # Name
        tk.Label(input_frame, text="Nama:", font=("Arial", 11), bg=self.bg_color).grid(
            row=0, column=0, sticky="w", pady=8
        )

        self.name_entry = tk.Entry(input_frame, font=("Arial", 11), width=30)
        self.name_entry.grid(row=0, column=1, pady=8, padx=10)

        # Weight
        tk.Label(
            input_frame, text="Berat Badan (kg):", font=("Arial", 11), bg=self.bg_color
        ).grid(row=1, column=0, sticky="w", pady=8)

        self.weight_entry = tk.Entry(input_frame, font=("Arial", 11), width=30)
        self.weight_entry.grid(row=1, column=1, pady=8, padx=10)

        # Height
        tk.Label(
            input_frame, text="Tinggi Badan (m):", font=("Arial", 11), bg=self.bg_color
        ).grid(row=2, column=0, sticky="w", pady=8)

        self.height_entry = tk.Entry(input_frame, font=("Arial", 11), width=30)
        self.height_entry.grid(row=2, column=1, pady=8, padx=10)

        # Buttons
        button_frame = tk.Frame(input_frame, bg=self.bg_color)
        button_frame.grid(row=3, column=0, columnspan=2, pady=15)

        self.calculate_btn = tk.Button(
            button_frame,
            text="Calculate & Save",
            font=("Arial", 11, "bold"),
            bg=self.primary_color,
            fg="black",
            width=15,
            height=1,
            cursor="hand2",
            command=self.calculate_bmi,
        )
        self.calculate_btn.pack(side=tk.LEFT, padx=5)

        self.clear_btn = tk.Button(
            button_frame,
            text="Clear",
            font=("Arial", 11),
            bg="#f44336",
            fg="black",
            width=10,
            height=1,
            cursor="hand2",
            command=self.clear_inputs,
        )
        self.clear_btn.pack(side=tk.LEFT, padx=5)

        # Result Section
        result_frame = tk.LabelFrame(
            main_frame,
            text="Result",
            font=("Arial", 12, "bold"),
            bg=self.bg_color,
            padx=20,
            pady=15,
        )
        result_frame.pack(fill=tk.X, pady=(0, 20))

        self.result_label = tk.Label(
            result_frame,
            text="Enter your data and click Calculate",
            font=("Arial", 12),
            bg=self.bg_color,
            fg="#666",
        )
        self.result_label.pack()

        # History Section
        history_frame = tk.LabelFrame(
            main_frame,
            text="History",
            font=("Arial", 12, "bold"),
            bg=self.bg_color,
            padx=10,
            pady=10,
        )
        history_frame.pack(fill=tk.BOTH, expand=True)

        # History text area with scrollbar
        self.history_text = scrolledtext.ScrolledText(
            history_frame, font=("Courier", 10), height=10, wrap=tk.WORD, bg="black"
        )
        self.history_text.pack(fill=tk.BOTH, expand=True)

        # Refresh button
        refresh_btn = tk.Button(
            history_frame,
            text="Refresh History",
            font=("Arial", 10),
            bg=self.secondary_color,
            fg="white",
            cursor="hand2",
            command=self.load_history,
        )
        refresh_btn.pack(pady=(10, 0))

    def calculate_bmi(self):
        try:
            name = self.name_entry.get().strip()
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())

            if not name:
                messagebox.showwarning("Warning", "Please enter your name!")
                return

            if weight <= 0 or height <= 0:
                messagebox.showwarning(
                    "Warning", "Weight and height must be positive numbers!"
                )
                return

            # Calculate BMI
            bmi = weight / (height**2)

            # Determine BMI category
            if bmi < 18.5:
                category = "Underweight"
                color = "#FF9800"
            elif 18.5 <= bmi < 25:
                category = "Normal"
                color = "#4CAF50"
            elif 25 <= bmi < 30:
                category = "Overweight"
                color = "#FF9800"
            else:
                category = "Obese"
                color = "#f44336"

            # Display result
            self.result_label.config(
                text=f"BMI: {bmi:.2f} - {category}",
                fg=color,
                font=("Arial", 14, "bold"),
            )

            # Save to file
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(self.data_file, "a") as file:
                file.write(
                    f"{timestamp} | {name} | BB: {weight} kg | TB: {height} m | BMI: {bmi:.2f} | {category}\n"
                )

            messagebox.showinfo(
                "Success",
                f"Data saved successfully!\n\nBMI: {bmi:.2f}\nCategory: {category}",
            )

            # Refresh history
            self.load_history()

            # Clear inputs
            self.clear_inputs()

        except ValueError:
            messagebox.showerror(
                "Error", "Please enter valid numbers for weight and height!"
            )

    def clear_inputs(self):
        self.name_entry.delete(0, tk.END)
        self.weight_entry.delete(0, tk.END)
        self.height_entry.delete(0, tk.END)
        self.name_entry.focus()

    def load_history(self):
        self.history_text.delete(1.0, tk.END)

        if not os.path.exists(self.data_file):
            self.history_text.insert(tk.END, "No history available yet.\n")
            return

        try:
            with open(self.data_file, "r") as file:
                lines = file.readlines()

            if not lines:
                self.history_text.insert(tk.END, "No history available yet.\n")
                return

            self.history_text.insert(tk.END, "=" * 80 + "\n")
            self.history_text.insert(tk.END, "BMI HISTORY\n")
            self.history_text.insert(tk.END, "=" * 80 + "\n\n")

            for i, line in enumerate(reversed(lines), 1):
                self.history_text.insert(tk.END, f"{i}. {line}")

            self.history_text.insert(tk.END, "\n" + "=" * 80 + "\n")
            self.history_text.insert(tk.END, f"Total Records: {len(lines)}\n")

        except Exception as e:
            self.history_text.insert(tk.END, f"Error loading history: {str(e)}\n")


def main():
    root = tk.Tk()
    app = BMIApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
