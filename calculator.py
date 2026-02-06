import tkinter as tk
from tkinter import font

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Calculator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # Variable to store the expression
        self.expression = ""
        
        # Create display
        self.display = tk.Entry(
            root,
            font=("Arial", 24),
            borderwidth=2,
            relief="solid",
            justify="right",
            bg="#f0f0f0"
        )
        self.display.pack(fill="both", padx=10, pady=10, ipady=10)
        
        # Create button frame
        button_frame = tk.Frame(root)
        button_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Button layout
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
            ["C", "←"]
        ]
        
        # Create buttons
        for row in buttons:
            row_frame = tk.Frame(button_frame)
            row_frame.pack(fill="both", expand=True, pady=5)
            
            for btn_text in row:
                if btn_text == "=":
                    btn = tk.Button(
                        row_frame,
                        text=btn_text,
                        font=("Arial", 20, "bold"),
                        bg="#4CAF50",
                        fg="white",
                        command=self.calculate
                    )
                elif btn_text == "C":
                    btn = tk.Button(
                        row_frame,
                        text=btn_text,
                        font=("Arial", 20, "bold"),
                        bg="#f44336",
                        fg="white",
                        command=self.clear
                    )
                elif btn_text == "←":
                    btn = tk.Button(
                        row_frame,
                        text=btn_text,
                        font=("Arial", 20, "bold"),
                        bg="#ff9800",
                        fg="white",
                        command=self.backspace
                    )
                elif btn_text in ["+", "-", "*", "/"]:
                    btn = tk.Button(
                        row_frame,
                        text=btn_text,
                        font=("Arial", 20, "bold"),
                        bg="#2196F3",
                        fg="white",
                        command=lambda x=btn_text: self.append_operator(x)
                    )
                else:
                    btn = tk.Button(
                        row_frame,
                        text=btn_text,
                        font=("Arial", 20),
                        bg="#e0e0e0",
                        command=lambda x=btn_text: self.append_digit(x)
                    )
                
                btn.pack(side="left", fill="both", expand=True, padx=5)
    
    def append_digit(self, digit):
        """Append digit or decimal point to the expression"""
        self.expression += str(digit)
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)
    
    def append_operator(self, operator):
        """Append operator to the expression"""
        if self.expression and self.expression[-1] not in ["+", "-", "*", "/"]:
            self.expression += operator
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expression)
    
    def calculate(self):
        """Evaluate the expression"""
        try:
            result = eval(self.expression)
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
            self.expression = str(result)
        except:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
            self.expression = ""
    
    def clear(self):
        """Clear the expression and display"""
        self.expression = ""
        self.display.delete(0, tk.END)
    
    def backspace(self):
        """Remove last character from expression"""
        self.expression = self.expression[:-1]
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
