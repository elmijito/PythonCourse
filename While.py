import tkinter as tk
from tkinter import messagebox

def ejecutar_while():
    try:
        inicio = int(entry_inicio.get())
        limite = int(entry_limite.get())
    except ValueError:
        messagebox.showerror("Error", "Ingresa solo números")
        return

    resultado.delete(1.0, tk.END)

    contador = inicio

    while contador <= limite:
        resultado.insert(tk.END, f"Iteración: contador = {contador}\n")
        contador += 1

    resultado.insert(tk.END, "El while terminó porque la condición ya no se cumple")

# Ventana principal
ventana = tk.Tk()
ventana.title("Demo While Loop en Python")
ventana.geometry("420x400")

# Labels y entradas
tk.Label(ventana, text="Valor inicial:").pack()
entry_inicio = tk.Entry(ventana)
entry_inicio.pack()

tk.Label(ventana, text="Valor límite:").pack()
entry_limite = tk.Entry(ventana)
entry_limite.pack()

# Botón
tk.Button(ventana, text="Iniciar While", command=ejecutar_while).pack(pady=10)

# Área de resultados
resultado = tk.Text(ventana, height=12, width=45)
resultado.pack()

ventana.mainloop()
