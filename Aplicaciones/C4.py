import customtkinter as ctk
import time

# 1. Configuración de la ventana estilo Streamer/Dark
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.geometry("450x300")
app.title("Nivel 3 - Detonador C4")

# 2. Elementos visuales (UI)
label_titulo = ctk.CTkLabel(app, text="💥 EXPLOSIVO C4 💥", font=("Arial", 28, "bold"), text_color="#ff4444")
label_titulo.pack(pady=20)

# El reloj digital en rojo
label_timer = ctk.CTkLabel(app, text="10", font=("Courier", 80, "bold"), text_color="#ff0000")
label_timer.pack(pady=10)

# 3. la logica del botón con el rango
def iniciar_conteo():
    boton_iniciar.configure(state="disable", text='DETONANDO...')
    for i in range (10, 0, -1):
        #formatearemos a los dígitos
        label_timer.configure(text=f"{i:02d}")

        #Obligamos a la interfaz a que actualice cada ciclo
        app.update()
        time.sleep(1) #Esperamos 1 segundo real
    
    label_timer.configure(text="¡BOOM!")
    app.configure(fg_color="#8D0505") #Parpadeo de la pantalla 
    boton_iniciar.configure(text = "SISTEMA DESTRUIDO")

boton_iniciar = ctk.CTkButton(
    app,
    text="ARM C4 (Iniciar conteo)",
    command = iniciar_conteo,
    font=("Arial", 16, "bold"),
    fg_color="#cc0000",
    hover_color="#990000"
)

boton_iniciar.pack(pady = 20)

# inicar aplicacion
app.mainloop()

