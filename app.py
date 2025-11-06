import tkinter as tk
import math

# -----------------------------
# BACKEND: Funções de cálculo
# -----------------------------
def calcular_expressao():
    try:
        expressao = entrada.get()
        resultado = eval(expressao)
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except Exception:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Erro")

def adicionar_valor(valor):
    entrada.insert(tk.END, valor)

def limpar():
    entrada.delete(0, tk.END)

def calcular_porcentagem():
    try:
        valor = float(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(valor / 100))
    except Exception:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Erro")

def calcular_raiz():
    try:
        valor = float(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(math.sqrt(valor)))
    except Exception:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Erro")

def calcular_seno():
    try:
        valor = float(entrada.get())
        resultado = math.sin(math.radians(valor))
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except Exception:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Erro")

def calcular_cosseno():
    try:
        valor = float(entrada.get())
        resultado = math.cos(math.radians(valor))
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except Exception:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Erro")

def calcular_tangente():
    try:
        valor = float(entrada.get())
        resultado = math.tan(math.radians(valor))
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except Exception:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Erro")

# -----------------------------
# FRONTEND: Interface gráfica
# -----------------------------
janela = tk.Tk()
janela.title("Calculadora Python")
janela.geometry("500x500")
janela.resizable(False, False)

entrada = tk.Entry(janela, width=20, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Teclas numéricas e operadores
botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('%', 4, 2), ('+', 4, 3)
]

for (texto, linha, coluna) in botoes:
    if texto == '%':
        tk.Button(janela, text=texto, width=5, height=2, command=calcular_porcentagem, font=("Arial", 14)).grid(row=linha, column=coluna, padx=5, pady=5)
    else:
        tk.Button(janela, text=texto, width=5, height=2, command=lambda t=texto: adicionar_valor(t), font=("Arial", 14)).grid(row=linha, column=coluna, padx=5, pady=5)

# Linha com funções especiais
tk.Button(janela, text="√", width=5, height=2, command=calcular_raiz, font=("Arial", 14)).grid(row=5, column=0, padx=5, pady=5)
tk.Button(janela, text="sin", width=5, height=2, command=calcular_seno, font=("Arial", 14)).grid(row=5, column=1, padx=5, pady=5)
tk.Button(janela, text="cos", width=5, height=2, command=calcular_cosseno, font=("Arial", 14)).grid(row=5, column=2, padx=5, pady=5)
tk.Button(janela, text="tan", width=5, height=2, command=calcular_tangente, font=("Arial", 14)).grid(row=5, column=3, padx=5, pady=5)

# Botões de controle
tk.Button(janela, text="C", width=11, height=2, command=limpar, font=("Arial", 14)).grid(row=6, column=0, columnspan=2, padx=5, pady=5)
tk.Button(janela, text="=", width=11, height=2, command=calcular_expressao, font=("Arial", 14)).grid(row=6, column=2, columnspan=2, padx=5, pady=5)

janela.mainloop()
