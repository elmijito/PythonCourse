import tkinter as tk

# Crear ventana grande
ventana = tk.Tk()
ventana.title("Calculadora Lambda PRO")
ventana.geometry("500x400")  # Tamaño grande
ventana.config(bg="#1e1e2f")  # Fondo oscuro elegante

# Fuente grande
FONT = ("Arial", 18)

# Input
entry = tk.Entry(
    ventana,
    font=("Arial", 22),
    justify="center",
    bd=5
)
entry.pack(pady=20, ipadx=10, ipady=10)

# Resultado
resultado = tk.Label(
    ventana,
    text="Resultado:",
    font=("Arial", 20, "bold"),
    fg="white",
    bg="#1e1e2f"
)
resultado.pack(pady=20)

# Función segura
def obtener_valor():
    try:
        return int(entry.get())
    except:
        return 0

# Frame para botones
frame_botones = tk.Frame(ventana, bg="#1e1e2f")
frame_botones.pack(pady=20)

# Estilo de botones
def crear_boton(texto, comando):
    return tk.Button(
        frame_botones,
        text=texto,
        command=comando,
        font=FONT,
        width=12,
        height=2,
        bg="#4CAF50",
        fg="white",
        activebackground="#45a049",
        bd=0
    )

# Botones con lambda 🔥
crear_boton(
    "Sumar 10",
    lambda: resultado.config(text=obtener_valor() + 10)
).grid(row=0, column=0, padx=10, pady=10)

crear_boton(
    "Duplicar",
    lambda: resultado.config(text=obtener_valor() * 2)
).grid(row=0, column=1, padx=10, pady=10)

crear_boton(
    "Restar 5",
    lambda: resultado.config(text=obtener_valor() - 5)
).grid(row=1, column=0, padx=10, pady=10)

crear_boton(
    "x3",
    lambda: resultado.config(text=obtener_valor() * 3)
).grid(row=1, column=1, padx=10, pady=10)

# Ejecutar
ventana.mainloop()