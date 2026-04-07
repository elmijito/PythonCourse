import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ---------------- ANIMACIÓN ----------------
def animar_texto(mensaje):
    resultado.configure(text="")  # limpia

    # efecto "escritura"
    for i in range(len(mensaje) + 1):
        texto_parcial = mensaje[:i]
        resultado.configure(text=texto_parcial)
        resultado.update()
        resultado.after(20)  # velocidad (más bajo = más rápido)

# ---------------- LÓGICA ----------------
def agenda_bandida():
    dia = entrada.get().lower()

    match dia:
        case "lunes":
            animar_texto("Salir con Arquímedes 😴")
        case "martes":
            animar_texto("Salir con Don Alfonso 🤔")
        case "miercoles":
            animar_texto("Sale con Rigoberto 😴")
        case "viernes":
            animar_texto("Sale con Bryan Sneider 🎉")
        case "domingo":
            animar_texto("Día de Día de descanso para buscar de Cristo 😌")
        case _:
            animar_texto("Día normal")

    animar_boton()

# ---------------- BOTÓN ANIMADO ----------------
def animar_boton():
    boton.configure(fg_color="#1f6aa5")  # color activo
    app.after(150, lambda: boton.configure(fg_color="#3a86ff"))

# ---------------- UI ----------------
app = ctk.CTk()
app.title("Agenda Bandida 🔥")
app.geometry("400x300")

titulo = ctk.CTkLabel(app, text="Agenda Misteriosa", font=("Arial", 20, "bold"))
titulo.pack(pady=20)

entrada = ctk.CTkEntry(app, placeholder_text="Escribe un día...")
entrada.pack(pady=10)

boton = ctk.CTkButton(app, text="Consultar", command=agenda_bandida)
boton.pack(pady=10)

resultado = ctk.CTkLabel(app, text="", font=("Arial", 16))
resultado.pack(pady=20)

app.mainloop()