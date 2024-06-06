import tkinter as tk
from tkinter import ttk, messagebox

class BMICalculator:
    def __init__(self, name, height_cm, weight_kg):
        self.name = name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def calculate_bmi(self):
        try:
            height_m = self.height_cm / 100
            bmi = self.weight_kg / (height_m ** 2)
            return round(bmi, 2)
        except ZeroDivisionError:
            return None

class BMICalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI 計算器")

        # 允許視窗可調整大小
        self.root.resizable(True, True)

        # 自動調整佈局
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)

        self.create_widgets()

    def create_widgets(self):
        # 姓名標籤和輸入框
        self.name_label = ttk.Label(self.root, text="姓名:", foreground="blue", font=("Arial", 10, "bold"))
        self.name_label.grid(column=0, row=0, padx=10, pady=5, sticky=tk.E)
        
        self.name_entry = ttk.Entry(self.root)
        self.name_entry.grid(column=1, row=0, padx=10, pady=5)

        # 身高標籤和輸入框
        self.height_label = ttk.Label(self.root, text="身高 (cm):", foreground="blue", font=("Arial", 10, "bold"))
        self.height_label.grid(column=0, row=1, padx=10, pady=5, sticky=tk.E)
        
        self.height_entry = ttk.Entry(self.root)
        self.height_entry.grid(column=1, row=1, padx=10, pady=5)

        # 體重標籤和輸入框
        self.weight_label = ttk.Label(self.root, text="體重 (kg):", foreground="blue", font=("Arial", 10, "bold"))
        self.weight_label.grid(column=0, row=2, padx=10, pady=5, sticky=tk.E)
        
        self.weight_entry = ttk.Entry(self.root)
        self.weight_entry.grid(column=1, row=2, padx=10, pady=5)

        # 計算按鈕
        self.calculate_button = ttk.Button(self.root, text="計算 BMI", command=self.calculate_bmi)
        self.calculate_button.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

        # BMI 結果標籤
        self.result_label = ttk.Label(self.root, text="BMI:", font=("Arial", 10, "bold"))
        self.result_label.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

    def calculate_bmi(self):
        try:
            name = self.name_entry.get()
            height_cm = float(self.height_entry.get())
            weight_kg = float(self.weight_entry.get())

            bmi_calculator = BMICalculator(name, height_cm, weight_kg)
            bmi = bmi_calculator.calculate_bmi()

            if bmi:
                self.result_label.config(text=f"BMI: {bmi}", foreground="red" if bmi >= 25 else "blue")
                self.show_bmi_category(bmi)
            else:
                self.result_label.config(text="BMI: 計算錯誤")
        except ValueError:
            messagebox.showerror("輸入錯誤", "請輸入有效的數字", "還是你小學沒畢業?")

    def show_bmi_category(self, bmi):
        if bmi < 18.5:
            category = "都不吃飯是不是想修仙阿....?"
        elif 18.5 <= bmi < 24.9:
            category = "Good Job, MDFK!"
        elif 25 <= bmi < 29.9:
            category = "該...減...月巴...了"
        else:
            category = "是不是想在地球上引發人類歷史上第一次完美的核融合??????"
        
        messagebox.showinfo("BMI 分類", f"你的 BMI 是 {bmi}， {category}")

def main():
    root = tk.Tk()
    app = BMICalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
