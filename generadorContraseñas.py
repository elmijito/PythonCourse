import tkinter as tk
# importa tkinter y lo renombra como 'tk' para construir la GUI (widgets, ventana, etc.)

from tkinter import ttk, messagebox
# importa 'ttk' (widgets con estilo) y 'messagebox' (diálogos tipo alerta)

import random
# módulo para operaciones aleatorias (usado para elegir caracteres)

import string
# módulo con constantes de caracteres (ascii_lowercase, digits, punctuation...)

class PasswordGeneratorApp:
    # define la clase principal de la aplicación (encapsula UI + lógica)
    def __init__(self, root):
        # constructor: recibe la ventana raíz (Tk)
        self.root = root
        # guarda la referencia a la ventana raíz en el objeto

        self.root.title("🔐 Generador de Contraseñas Pro")
        # establece el título de la ventana

        self.root.geometry("400x450")
        # define el tamaño inicial de la ventana (ancho x alto)

        self.root.resizable(False, False)
        # evita que el usuario cambie el tamaño (ancho y alto fijos)

        # --- VARIABLES DE ESTADO ---
        # Guardamos la configuración del usuario aquí

        self.length_var = tk.IntVar(value=12)
        # variable entera ligada a la UI para la longitud de la contraseña (valor por defecto 12)

        self.use_upper = tk.BooleanVar(value=True)
        # BooleanVar ligado al checkbox: incluir mayúsculas (por defecto True)

        self.use_numbers = tk.BooleanVar(value=True)
        # BooleanVar ligado al checkbox: incluir números (por defecto True)

        self.use_symbols = tk.BooleanVar(value=False)
        # BooleanVar ligado al checkbox: incluir símbolos (por defecto False)

        self.password_var = tk.StringVar()
        # StringVar para mostrar la contraseña generada en el Entry (vinculado a la UI)

        # --- INTERFAZ GRÁFICA (UI) ---
        self.create_widgets()
        # llama al método que crea y empaqueta todos los widgets en la ventana

    def create_widgets(self):
        # método que construye la interfaz gráfica

        # 1. Título y Estilo
        title_label = ttk.Label(self.root, text="Password Generator", font=("Helvetica", 16, "bold"))
        # etiqueta con texto grande para el título (usa ttk para mejor apariencia)

        title_label.pack(pady=20)
        # empaqueta la etiqueta en la ventana con margen vertical (padding Y)

        # 2. Área de visualización de la contraseña
        display_frame = ttk.LabelFrame(self.root, text="Tu Contraseña")
        # crea un frame con borde y título que agrupa la visualización de la contraseña

        display_frame.pack(pady=10, padx=20, fill="x")
        # empaqueta el frame con padding y lo hace expandir horizontalmente

        self.entry_password = ttk.Entry(
            display_frame, 
            textvariable=self.password_var, 
            font=("Consolas", 14), 
            state="readonly",  # Solo lectura para que no la editen a mano
            justify="center"
        )
        # Entry (campo de texto) dentro del frame para mostrar la contraseña;
        # vinculado a self.password_var, tipo de letra monoespaciada, solo lectura, centrado

        self.entry_password.pack(pady=10, padx=10, fill="x")
        # empaqueta el Entry con padding y lo hace expandir horizontalmente

        # 3. Controles de Configuración
        settings_frame = ttk.LabelFrame(self.root, text="Configuración")
        # frame con título para agrupar controles (slider, checkboxes)

        settings_frame.pack(pady=10, padx=20, fill="x")
        # empaqueta el frame con padding y expansión horizontal

        # Slider de longitud
        lbl_length = ttk.Label(settings_frame, text="Longitud: 12 caracteres")
        # etiqueta que muestra la longitud actual (se actualizará dinámicamente)

        lbl_length.pack(pady=(10, 0))
        # empaqueta la etiqueta con padding superior

        # Función lambda pequeña para actualizar la etiqueta cuando muevan el slider
        scale_length = ttk.Scale(
            settings_frame, 
            from_=6, to=32, 
            variable=self.length_var, 
            orient="horizontal",
            command=lambda v: lbl_length.config(text=f"Longitud: {int(float(v))} caracteres")
        )
        # slider (escala) de 6 a 32 que controla self.length_var;
        # el 'command' recibe el valor como string/float y actualiza lbl_length en tiempo real

        scale_length.pack(pady=5, padx=10, fill="x")
        # empaqueta el slider con padding y expansión horizontal

        # Checkboxes
        chk_upper = ttk.Checkbutton(settings_frame, text="Incluir Mayúsculas (A-Z)", variable=self.use_upper)
        # checkbox para incluir mayúsculas, ligado a self.use_upper

        chk_upper.pack(anchor="w", padx=20)
        # empaqueta el checkbox alineado a la izquierda con padding horizontal

        chk_num = ttk.Checkbutton(settings_frame, text="Incluir Números (0-9)", variable=self.use_numbers)
        # checkbox para incluir números, ligado a self.use_numbers

        chk_num.pack(anchor="w", padx=20)
        # empaqueta el checkbox alineado a la izquierda con padding horizontal

        chk_sym = ttk.Checkbutton(settings_frame, text="Incluir Símbolos (@#$%)", variable=self.use_symbols)
        # checkbox para incluir símbolos especiales, ligado a self.use_symbols

        chk_sym.pack(anchor="w", padx=20, pady=(0, 10))
        # empaqueta el checkbox con padding inferior adicional

        # 4. Botones de Acción
        actions_frame = ttk.Frame(self.root)
        # frame simple para agrupar botones de acción

        actions_frame.pack(pady=20)
        # empaqueta el frame con margen vertical

        btn_generate = ttk.Button(actions_frame, text="🔄 Generar", command=self.generate_password)
        # botón que ejecuta self.generate_password cuando se hace clic

        btn_generate.pack(side="left", padx=10)
        # empaqueta el botón a la izquierda con separación horizontal

        btn_copy = ttk.Button(actions_frame, text="📋 Copiar", command=self.copy_to_clipboard)
        # botón que copia la contraseña al portapapeles al hacer clic

        btn_copy.pack(side="left", padx=10)
        # empaqueta el botón a la izquierda junto al anterior

        # 5. Etiqueta de estado (Feedback al usuario)
        self.status_label = ttk.Label(self.root, text="Listo para generar", foreground="gray")
        # etiqueta en la parte inferior para mensajes de estado/feedback (color gris por defecto)

        self.status_label.pack(side="bottom", pady=10)
        # empaqueta la etiqueta en la parte inferior con padding

    def generate_password(self):
        # método que crea la contraseña según la configuración seleccionada
        try:
            # 1. Definir los caracteres base (siempre minúsculas)
            characters = string.ascii_lowercase
            # empieza con todas las letras minúsculas (a-z)

            # 2. Agregar complejidad según lo que eligió el usuario
            if self.use_upper.get():
                characters += string.ascii_uppercase
            # si el usuario marcó mayúsculas, añádelas (A-Z)

            if self.use_numbers.get():
                characters += string.digits
            # si marcó números, añade dígitos (0-9)

            if self.use_symbols.get():
                characters += string.punctuation
            # si marcó símbolos, añade todos los signos de puntuación disponibles

            # 3. Generar la contraseña
            length = self.length_var.get()
            # obtiene la longitud deseada desde la variable ligada al slider

            password = "".join(random.choice(characters) for _ in range(length))
            # construye la contraseña: elige aleatoriamente 'length' caracteres de la cadena 'characters'
            # NOTA: si 'characters' está vacío, random.choice lanzará IndexError

            # 4. Mostrar en pantalla
            self.password_var.set(password)
            # actualiza la StringVar ligada al Entry para mostrar la contraseña

            self.status_label.config(text="¡Contraseña generada!", foreground="green")
            # actualiza la etiqueta de estado para indicar éxito (texto en verde)
        
        except IndexError:
            # Esto pasa si el usuario desmarca TODO y la lista de caracteres queda vacía
            messagebox.showwarning("Error", "¡Debes seleccionar al menos un tipo de caracter!")
            # muestra un diálogo de advertencia explicando que no hay caracteres disponibles

            self.status_label.config(text="Error de configuración", foreground="red")
            # actualiza la etiqueta de estado a error (texto en rojo)

    def copy_to_clipboard(self):
        # método que copia la contraseña actual al portapapeles del sistema
        password = self.password_var.get()
        # obtiene la contraseña desde la StringVar

        if password:
            # si hay algo en la contraseña
            self.root.clipboard_clear()
            # limpia el portapapeles actual

            self.root.clipboard_append(password)
            # añade la contraseña al portapapeles

            self.status_label.config(text="¡Copiado al portapapeles!", foreground="blue")
            # feedback al usuario indicando copia (color azul)
        else:
            # si no hay contraseña generada aún
            self.status_label.config(text="Primero genera una contraseña", foreground="red")
            # indica al usuario que primero debe generar una contraseña

# --- PUNTO DE ENTRADA ---
if __name__ == "__main__":
    # bloque que asegura que el código solo corra si el script es el principal (no cuando se importa)

    root = tk.Tk()
    # crea la ventana principal de la aplicación

    # Tema visual (opcional, intenta adaptarse al SO)
    style = ttk.Style()
    # instancia de estilo para widgets ttk

    style.theme_use('clam') 
    # aplica el tema 'clam' (puede cambiar la apariencia; si no existe puede lanzar excepción en algunos sistemas)

    app = PasswordGeneratorApp(root)
    # instancia la aplicación, construyendo la UI y enlazando todo

    root.mainloop()
    # inicia el loop principal de la interfaz gráfica (espera eventos y mantiene la ventana abierta)
