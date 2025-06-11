import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.configure(background="#f0f4f8")

        self.expression = tk.StringVar()
        self.expression.set("")

        self.create_widgets()
        self.root.bind("<Key>", self.key_press)

    def create_widgets(self):
        # Titlu
        title = tk.Label(self.root, text="Calculator", font=("Helvetica", 16, "bold"), bg="#f0f4f8")
        title.grid(row=0, column=0, columnspan=4, pady=10)

        # Ecranul de afișare
        result_label = tk.Label(self.root, textvariable=self.expression, font=("Arial", 18), bg="#f0f4f8", fg="#333")
        result_label.grid(row=1, column=0, columnspan=4, sticky="we", padx=10, pady=10)

        # Butoane numerice
        buttons = [
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2),
            ('0', 5, 1)
        ]
        for (text, r, c) in buttons:
            btn = tk.Button(self.root, text=text, font=("Arial", 10, "bold"), bg="#4caf50", fg="white",
                            padx=10, pady=5, command=lambda t=text: self.add_to_expression(t))
            btn.grid(row=r, column=c, padx=5, pady=5, sticky="we")

        # Butoane operatori
        operators = [
            ('+', 2, 3), ('-', 3, 3), ('*', 4, 3), ('/', 5, 3)
        ]
        for (op, r, c) in operators:
            btn = tk.Button(self.root, text=op, padx=10, pady=5, command=lambda o=op: self.add_to_expression(o))
            btn.grid(row=r, column=c, padx=5, pady=5, sticky="we")

        # Buton egal
        eq_btn = tk.Button(self.root, text='=', padx=10, pady=5, command=self.evaluate_expression)
        eq_btn.grid(row=5, column=2, padx=5, pady=5, sticky="we")

        # Buton Clear
        clear_btn = tk.Button(self.root, text='C', padx=10, pady=5, command=self.clear_expression)
        clear_btn.grid(row=5, column=0, padx=5, pady=5, sticky="we")

    def add_to_expression(self, value):
        current = self.expression.get()
        self.expression.set(current + value)

    def clear_expression(self):
        self.expression.set("")

    def evaluate_expression(self):
        expr = self.expression.get()
        if not expr:
            return
        if expr[-1] in "+-*/":
            self.expression.set("Syntax Error")
            return
        try:
            # WARNING: eval is unsafe in production, only use here for simplicity
            result = eval(expr)
            self.expression.set(str(result))
        except ZeroDivisionError:
            self.expression.set("Division by 0")
        except Exception:
            self.expression.set("Error")

    def key_press(self, event):
        char = event.char
        if char in "0123456789+-*/":
            self.add_to_expression(char)
        elif char == "\r":  # Enter
            self.evaluate_expression()
        elif char.lower() == "c":
            self.clear_expression()


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
