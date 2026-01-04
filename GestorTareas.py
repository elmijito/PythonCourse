# --- 1. Importaciones Necesarias ---

import tkinter as tk  # Importamos la librería principal para crear la interfaz gráfica (GUI).
from tkinter import font as tkfont # Importamos 'font' para darle un estilo moderno al texto.
import json           # Importamos 'json' para guardar y cargar las tareas en un formato estructurado.
import os             # Importamos 'os' para interactuar con el sistema, verificando si el archivo existe.

# --- 2. Configuración del Archivo ---

FILE = "tasks.json" # Definimos el nombre del archivo donde se guardarán las tareas permanentemente.

# --- 3. Funciones de Carga y Guardado (Persistencia de Datos) ---

def load_tasks():
    """Función para cargar las tareas guardadas desde el archivo JSON al iniciar la aplicación."""
    if os.path.exists(FILE):
        # Si el archivo existe, lo abrimos en modo lectura ("r").
        with open(FILE, "r") as f:
            return json.load(f) # Leemos y cargamos el contenido (la lista de tareas).
    return [] # Si el archivo no existe (primera vez que se usa), devolvemos una lista vacía.

def save_tasks(tasks):
    """Función para guardar la lista actual de tareas en el archivo JSON."""
    # Abrimos el archivo en modo escritura ("w").
    with open(FILE, "w") as f:
        # Usamos 'json.dump' para escribir la lista 'tasks' en el archivo, guardando el progreso.
        json.dump(tasks, f, indent=4) # Agregamos 'indent=4' para que el archivo sea más legible.

# --- 4. Funciones de Interfaz (GUI - Lo que la gente ve en el live) ---

def add_task():
    """Función que se llama cuando se pulsa el botón 'Agregar'."""
    # Obtenemos el texto ingresado por el usuario en el campo de entrada.
    task = entry.get()
    if task:
        # Si el texto no está vacío:
        tasks.append(task) # 1. Agregamos la tarea a la lista de Python.
        # 2. Insertamos la tarea al final (tk.END) del Listbox (la caja visible).
        listbox.insert(tk.END, task) 
        save_tasks(tasks) # 3. Guardamos la lista actualizada en el archivo.
        entry.delete(0, tk.END) # 4. Limpiamos el campo de entrada para la siguiente tarea.

def delete_task():
    """Función que se llama cuando se pulsa el botón 'Eliminar'."""
    # Obtenemos la tupla de índices de los elementos seleccionados en el Listbox.
    selected = listbox.curselection()
    if selected:
        # Si hay algo seleccionado:
        idx = selected[0] # Tomamos el primer índice seleccionado.
        tasks.pop(idx) # 1. Eliminamos la tarea de la lista de Python usando el índice.
        listbox.delete(idx) # 2. Eliminamos la tarea del Listbox (la caja visible) por índice.
        save_tasks(tasks) # 3. Guardamos la lista actualizada en el archivo.

# --- 5. Configuración de la Ventana Principal (Root) ---

root = tk.Tk() # Creamos la ventana principal de la aplicación.
root.title("✨ Gestor de Tareas TikTok Live ✨") # Cambiamos el título por uno más atractivo.

# --- 6. Estilos Visuales (¡Haciéndolo más llamativo!) ---

# Definimos una fuente más grande y en negrita para los botones y títulos.
app_font = tkfont.Font(family="Helvetica", size=12, weight="bold")
bg_color = "#282c34" # Un color de fondo oscuro, moderno (como un tema de programación).
fg_color = "#abb2bf" # Color de texto claro.
btn_color = "#61afef" # Color azul llamativo para los botones.
list_bg = "#3e4452" # Color de fondo para la lista.

root.config(bg=bg_color) # Aplicamos el color de fondo a la ventana principal.

# --- 7. Inicialización de Datos y Variables ---

tasks = load_tasks() # Cargamos las tareas guardadas al inicio.

# --- 8. Creación de Widgets (Elementos de la Interfaz) ---

# Campo de entrada (donde el usuario escribe la tarea)
entry = tk.Entry(root, width=40, font=('Helvetica', 12), bd=2, relief=tk.FLAT, bg="#5c6370", fg="white", insertbackground='white')
entry.pack(pady=15, padx=20) # 'pady' y 'padx' dan espacio alrededor.

# Botón Agregar
add_btn = tk.Button(root, text="➕ Agregar Tarea", command=add_task, 
                    font=app_font, bg=btn_color, fg=bg_color, relief=tk.FLAT, width=20, padx=10, pady=5)
add_btn.pack(pady=5)

# Botón Eliminar
del_btn = tk.Button(root, text="❌ Eliminar Tarea", command=delete_task, 
                    font=app_font, bg="#e06c75", fg=bg_color, relief=tk.FLAT, width=20, padx=10, pady=5)
del_btn.pack(pady=5)

# Listbox (La caja donde se muestran las tareas)
listbox = tk.Listbox(root, width=50, height=12, font=('Courier New', 10), 
                     bg=list_bg, fg=fg_color, selectbackground="#98c379", selectforeground=bg_color, 
                     highlightthickness=0) # Quitamos el borde de enfoque.
listbox.pack(pady=15, padx=20)

# --- 9. Cargar Tareas en el Listbox (Visualización Inicial) ---

# Recorremos la lista de tareas cargadas y las mostramos una por una en el Listbox.
for t in tasks:
    listbox.insert(tk.END, t)

# --- 10. Bucle Principal ---

# Esta línea inicia el bucle de la interfaz gráfica. Es lo que mantiene la ventana abierta
# y esperando interacciones del usuario (clics en botones, etc.). ¡Fundamental!
root.mainloop()