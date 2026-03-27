# Importamos tkinter, la librería estándar para interfaces gráficas en Python
import tkinter as tk

# Importamos messagebox para mostrar alertas emergentes
from tkinter import messagebox

# Creamos la ventana principal de la aplicación
ventana = tk.Tk()

# Definimos el título de la ventana
ventana.title("Gestor de Gastos Personales")

# Definimos el tamaño de la ventana (ancho x alto)
ventana.geometry("400x400")

# Creamos una lista vacía donde se guardarán los gastos
gastos = []

# ---------------- FUNCIONES ----------------

# Función para agregar un gasto
def agregar_gasto():
    # Obtenemos el texto ingresado en el campo de concepto
    concepto = entry_concepto.get()

    # Obtenemos el texto ingresado en el campo de monto
    monto = entry_monto.get()

    # Validamos que los campos no estén vacíos
    if concepto == "" or monto == "":
        messagebox.showwarning("Error", "Todos los campos son obligatorios")
        return

    # Intentamos convertir el monto a número decimal
    try:
        monto = float(monto)
    except:
        messagebox.showerror("Error", "El monto debe ser un número")
        return

    # Creamos un diccionario con el gasto
    gasto = {
        "concepto": concepto,
        "monto": monto
    }

    # Agregamos el gasto a la lista de gastos
    gastos.append(gasto)

    # Mostramos el gasto en la lista visual
    lista_gastos.insert(tk.END, f"{concepto} - ${monto}")

    # Limpiamos los campos de texto
    entry_concepto.delete(0, tk.END)
    entry_monto.delete(0, tk.END)

    # Actualizamos el total
    actualizar_total()

# Función para calcular y mostrar el total de gastos
def actualizar_total():
    # Sumamos todos los montos de los gastos
    total = sum(gasto["monto"] for gasto in gastos)

    # Actualizamos el texto del label del total
    label_total.config(text=f"Total: ${total}")

# ---------------- INTERFAZ ----------------

# Etiqueta para el concepto
label_concepto = tk.Label(ventana, text="Concepto:")
label_concepto.pack()

# Campo de texto para el concepto
entry_concepto = tk.Entry(ventana)
entry_concepto.pack()

# Etiqueta para el monto
label_monto = tk.Label(ventana, text="Monto:")
label_monto.pack()

# Campo de texto para el monto
entry_monto = tk.Entry(ventana)
entry_monto.pack()

# Botón para agregar el gasto
btn_agregar = tk.Button(ventana, text="Agregar gasto", command=agregar_gasto)
btn_agregar.pack(pady=10)

# Lista donde se mostrarán los gastos
lista_gastos = tk.Listbox(ventana)
lista_gastos.pack(fill=tk.BOTH, expand=True)

# Etiqueta que muestra el total de gastos
label_total = tk.Label(ventana, text="Total: $0")
label_total.pack(pady=10)

# Ejecutamos el loop principal de la aplicación
ventana.mainloop()
