import tkinter as tk
from tkinter import messagebox
from openpyxl import Workbook

#crear un libro de excel
wb = Workbook()
ws = wb.active
ws.append(["Nombre","Edad","Email","Telefono","Dirección"])

def guardar_datos():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    email = entry_Email.get()
    telefono = entry_telefono.get()
    direccion = entry_direccion.get()


if not nombre or not edad or not email or not telefono or not direccion:
        messagebox.showwarning("Campos incompletos", "Por favor, complete todos los campos.")
        return

root = tk.Tk()
root.title("Formulario de Entrada de Datos")
root.configure(bg='#4B6587')
label_style = {"bg": '#4B6587', "fg": "white"}
entry_style = {"bg": '#D3D3D3', "fg": "black"}

label_nombre = tk.Label(root, text="Nombre:", **label_style)
label_nombre.grid(row=0, column=0, padx=10, pady= 5)
entry_nombre = tk.Entry(root, **entry_style)
entry_nombre.grid(row=0, column=1, padx=10, pady=5)    

label_edad = tk.Label(root, text="Edad:", **label_style)
label_edad.grid(row=1, column=0, padx=10, pady= 5)
entry_edad = tk.Entry(root, **entry_style)
entry_edad.grid(row=1, column=1, padx=10, pady=5)

label_Email = tk.Label(root, text="Email:", **label_style)
label_Email.grid(row=2, column=0, padx=10, pady= 5)
entry_Email = tk.Entry(root, **entry_style)
entry_Email.grid(row=2, column=1, padx=10, pady=5)

label_telefono = tk.Label(root, text="Telefono:", **label_style)
label_telefono.grid(row=3, column=0, padx=10, pady= 5)
entry_telefono = tk.Entry(root, **entry_style)
entry_telefono.grid(row=3, column=1, padx=10, pady=5)

label_direccion = tk.Label(root, text="Dirección:", **label_style)
label_direccion.grid(row=4, column=0, padx=10, pady= 5)
entry_direccion = tk.Entry(root, **entry_style)
entry_direccion.grid(row=4, column=1, padx=10, pady=5)

boton_guardar = tk.Button(root, text="Guardar", bg='#1E90FF', fg='white', command=guardar_datos, bg='#6D8299', fg='white')
boton_guardar.grid(row=5, column=0, columnspan=3, padx=10 pady=10)


root.mainloop()


