import tkinter as tk
from tkinter import messagebox  

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.resizable(False, False)
        self.root.configure(bg="lightblue")
        self.root.geometry("375x550")

        # Variable para almacenar el resultado
        
    
        self.entrada = tk.Entry( self.root, width=17, font=("Arial", 28), borderwidth=0,
                                relief='solid', bg="lightblue", justify='right')
        self.entrada.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=10, pady=(10,5))
        self.create_buttons()

        def create_buttons(self):
            botones = [
                 ('c',2) (' +',1), ('-',1), ('/',1),
                    ('7',1), ('8',1), ('9',1), ('*',1),
                    ('4',1), ('5',1), ('6',1), ('%',1),
                    ('1',1), ('2',1), ('3',1), ('=',2),
                    ('0',2), ('+',1), ('-',1), ('/',1) 
            ]
            colores_botones  = {
                'c': 'red',
                '=': 'green',
                '+': 'lightgray',
                '-': 'lightgray',
                '*': 'lightgray',
                '/': 'lightgray',
                '%': 'lightgray'
            }

            frame_botones = tk.Frame(self.root, bg="lightblue")
            frame_botones.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

            fila = 0
            columna = 0

            for boton, span in botones:
                color = colores_botones.get(boton, "lightgray")
                b = tk.Button(frame_botones, text=boton, width=5, height=2, font=("Arial", 18),
                              command=lambda b=boton: self.on_button_click(b), bg=color)
                b.grid(row=fila, column=columna, columnspan=span, sticky="nsew", padx=5, pady=5)
                columna += span
                if columna >= 4:
                    columna = 0
                    fila += 1 

                    #