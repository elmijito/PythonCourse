import tkinter as tk

# Decorador
def mayusculas(func):
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        return resultado.upper()
    return wrapper

# Función decorada
@mayusculas
def obtener_texto():
    return entrada.get()

# Función del botón
def mostrar():
    resultado = obtener_texto()
    etiqueta_resultado.config(text=resultado)

# Ventana
ventana = tk.Tk()
ventana.title("Decoradores en acción")

# Input
entrada = tk.Entry(ventana)
entrada.pack()

# Botón
boton = tk.Button(ventana, text="Transformar", command=mostrar)
boton.pack()

# Resultado
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack()

ventana.mainloop()