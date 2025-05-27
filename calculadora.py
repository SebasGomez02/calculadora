import tkinter as tk
from tkinter import messagebox, Scrollbar
import math

class CalculadoraCientifica:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Científica con Historial")
        self.root.resizable(False, False)
        self.root.configure(bg="lightblue")
        self.root.geometry("750x500")

        # Campo de entrada principal
        self.entrada = tk.Entry(self.root, width=25, font=("Arial", 24), borderwidth=0,
                                relief='solid', bg="lightblue", justify='right')
        self.entrada.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=10, pady=(10, 5))

        # Historial (zona de texto scrollable)
        self.historial_label = tk.Label(self.root, text="Historial", bg="lightblue", font=("Arial", 12, "bold"))
        self.historial_label.grid(row=0, column=4, padx=10)

        self.historial = tk.Text(self.root, width=25, height=26, font=("Arial", 10), state='disabled')
        self.historial.grid(row=1, column=4, rowspan=5, padx=10, pady=5)

        self.scroll = Scrollbar(self.root, command=self.historial.yview)
        self.scroll.grid(row=1, column=5, rowspan=5, sticky='ns')
        self.historial.config(yscrollcommand=self.scroll.set)

        self.create_buttons()

    def create_buttons(self):
        botones = [
            ('c', 1), ('(', 1), (')', 1), ('%', 1), ('√', 1),
            ('7', 1), ('8', 1), ('9', 1), ('/', 1), ('^', 1),
            ('4', 1), ('5', 1), ('6', 1), ('*', 1), ('π', 1),
            ('1', 1), ('2', 1), ('3', 1), ('-', 1), ('log', 1),
            ('0', 1), ('.', 1), ('=', 1), ('+', 1), ('sin', 1),
            ('cos', 1), ('tan', 1), ('ln', 1), ('!', 1),
            ('ClrHist', 5)  # Limpiar historial
        ]

        color_funciones = {
            'c': 'red', '=': 'green', '+': 'lightgray', '-': 'lightgray',
            '*': 'lightgray', '/': 'lightgray', '%': 'lightgray',
            '^': 'lightgray', '√': 'lightgray', '!': 'lightgray',
            'π': 'lightgray', 'log': 'lightgray', 'ln': 'lightgray',
            'sin': 'lightgray', 'cos': 'lightgray', 'tan': 'lightgray',
            'ClrHist': '#FFDD99'
        }

        frame = tk.Frame(self.root, bg="lightblue")
        frame.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

        fila = 0
        columna = 0
        for texto, span in botones:
            color = color_funciones.get(texto, "white")
            boton = tk.Button(frame, text=texto, width=5 * span, height=2,
                              font=("Arial", 12), bg=color, relief='ridge',
                              command=lambda t=texto: self.on_click(t))
            boton.grid(row=fila, column=columna, columnspan=span, padx=3, pady=3)
            columna += span
            if columna >= 5:
                fila += 1
                columna = 0

    def on_click(self, valor):
        if valor == 'c':
            self.entrada.delete(0, tk.END)
        elif valor == 'ClrHist':
            self.historial.config(state='normal')
            self.historial.delete(1.0, tk.END)
            self.historial.config(state='disabled')
        elif valor == '=':
            try:
                expresion = self.entrada.get()
                resultado = self.evaluar_expresion(expresion)
                self.entrada.delete(0, tk.END)
                self.entrada.insert(0, str(resultado))
                self.agregar_a_historial(expresion, resultado)
            except Exception as e:
                messagebox.showerror("Error", f"Expresión no válida:\n{str(e)}")
        else:
            if valor == 'π':
                valor = str(math.pi)
            elif valor == '^':
                valor = '**'
            elif valor == '√':
                valor = 'math.sqrt('
            elif valor == 'log':
                valor = 'math.log10('
            elif valor == 'ln':
                valor = 'math.log('
            elif valor == 'sin':
                valor = 'math.sin(math.radians('
            elif valor == 'cos':
                valor = 'math.cos(math.radians('
            elif valor == 'tan':
                valor = 'math.tan(math.radians('
            elif valor == '!':
                valor = 'math.factorial('

            self.entrada.insert(tk.END, valor)

    def evaluar_expresion(self, expresion):
        abierta = expresion.count('(')
        cerrada = expresion.count(')')
        if abierta > cerrada:
            expresion += ')' * (abierta - cerrada)
        return eval(expresion, {"__builtins__": None, "math": math})

    def agregar_a_historial(self, operacion, resultado):
        self.historial.config(state='normal')
        self.historial.insert(tk.END, f"{operacion} = {resultado}\n")
        self.historial.see(tk.END)
        self.historial.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraCientifica(root)
    root.mainloop()
