import tkinter as tk
from ttkthemes import ThemedTk
from tkinter import ttk

class window(ThemedTk):
    def __init__(self, theme:str|None,  **kwargs):
        super().__init__(**kwargs)
        self.title('BMI計算器')
        self.configure(bg='#D3D3D3')
        self.geometry('350x350')
        self.resizable(False, False)
        style = ttk.Style()
        # print(ttk.Style.theme_names())

        mainFrame = ttk.Frame(self)
        title_label = ttk.Label(self, text='BMI計算', font=('Ariel', 16) )
        title_label.pack(pady=10)
        mainFrame.pack(padx=100, pady=50)

def main():
    windows = window(theme='arc')
    windows.mainloop()
    
if __name__ == '__main__':
    main()
