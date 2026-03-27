import tkinter as tk
from tkinter import scrolledtext

# ---------------- EJEMPLOS ---------------- #

def example_functions():
    code = """
def saludar():
    return "Hola programador!"

resultado = saludar()
print(resultado)
"""
    result = "Hola programador!"
    return code, result


def example_arguments():
    code = """
def sumar(a, b):
    return a + b

print(sumar(5,3))
"""
    result = str(5 + 3)
    return code, result


def example_args_kwargs():
    code = """
def mostrar(*args, **kwargs):
    print(args)
    print(kwargs)

mostrar(1,2,3, nombre="Juan", edad=25)
"""
    result = "(1, 2, 3)\n{'nombre': 'Juan', 'edad': 25}"
    return code, result


def example_scope():
    code = """
x = 10

def mostrar():
    print(x)

mostrar()
"""
    result = "10"
    return code, result


def example_lambda():
    code = """
doble = lambda x: x * 2
print(doble(5))
"""
    result = "10"
    return code, result


def example_recursion():
    code = """
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))
"""
    result = "120"
    return code, result


def example_generators():
    code = """
def contador():
    for i in range(3):
        yield i

for num in contador():
    print(num)
"""
    result = "0\n1\n2"
    return code, result


# ---------------- INTERFAZ ---------------- #

def mostrar_ejemplo(func):
    code, result = func()

    code_area.delete(1.0, tk.END)
    code_area.insert(tk.END, code)

    result_area.delete(1.0, tk.END)
    result_area.insert(tk.END, result)


root = tk.Tk()
root.title("Python Functions Explorer")
root.geometry("800x500")

# Panel izquierdo (botones)
frame_buttons = tk.Frame(root)
frame_buttons.pack(side="left", padx=10, pady=10)

tk.Label(frame_buttons, text="Temas", font=("Arial", 14)).pack(pady=5)

tk.Button(frame_buttons, text="Functions",
          command=lambda: mostrar_ejemplo(example_functions)).pack(fill="x")

tk.Button(frame_buttons, text="Arguments",
          command=lambda: mostrar_ejemplo(example_arguments)).pack(fill="x")

tk.Button(frame_buttons, text="*args **kwargs",
          command=lambda: mostrar_ejemplo(example_args_kwargs)).pack(fill="x")

tk.Button(frame_buttons, text="Scope",
          command=lambda: mostrar_ejemplo(example_scope)).pack(fill="x")

tk.Button(frame_buttons, text="Lambda",
          command=lambda: mostrar_ejemplo(example_lambda)).pack(fill="x")

tk.Button(frame_buttons, text="Recursion",
          command=lambda: mostrar_ejemplo(example_recursion)).pack(fill="x")

tk.Button(frame_buttons, text="Generators",
          command=lambda: mostrar_ejemplo(example_generators)).pack(fill="x")


# Panel derecho
frame_right = tk.Frame(root)
frame_right.pack(side="right", expand=True, fill="both", padx=10, pady=10)

tk.Label(frame_right, text="Código").pack()

code_area = scrolledtext.ScrolledText(frame_right, height=12)
code_area.pack (fill="both", expand=True)

tk.Label(frame_right, text="Resultado").pack()

result_area = scrolledtext.ScrolledText(frame_right, height=6)
result_area.pack(fill="both",expand=True)

root.mainloop()




