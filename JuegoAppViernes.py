import tkinter as tk
import random

opciones = ["Piedra", "Papel", "Tijera"]
def jugar(eleccion_usuario):
    eleccion_pc = random.choice(opciones) #eleccion aleatoria de la pc
    if eleccion_usuario == eleccion_pc:
        resultado = "¡Empate!"
    elif (eleccion_usuario == "Piedra" and eleccion_pc == "Tijera") or \
         (eleccion_usuario == "Papel" and eleccion_pc == "Piedra") or \
         (eleccion_usuario == "Tijera" and eleccion_pc == "Papel"):
        resultado = f"¡Ganaste! {eleccion_usuario} vence a {eleccion_pc}."
    else:
        resultado = f"Perdiste"

    etiqueta_resultado.config(text=f"Tú{eleccion_usuario} PC: {eleccion_pc}\n{resultado}")

ventana = tk.Tk() #Creacion de la ventana
ventana.title("Piedra, Papel o Tijera") #Boton de título
ventana.geometry("500x300") #dimensiones de la ventana



font = ("Arial", 16) # cambia la fuente y tamaño de la letra
    # pack(pady=10) # espacio vertical (eliminado porque no está asociado a ningún widget)

frame_botones = tk.Frame(ventana) #crea un frame para los botones
frame_botones.pack() #espacio vertical

for opcion in opciones:
    boton = tk.Button(frame_botones, text=opcion, width=10, font=("Arial", 14),
                        command=lambda o=opcion: jugar(o)) #lambda para pasar la opción al comando
    boton.pack(side=tk.LEFT, padx=10) #añade los botones al frame y espacio horizontal


etiqueta_resultado = tk.Label(ventana, text=f"", font=("Arial", 14), pady=20) #crea una etiqueta para mostrar el resultado
etiqueta_resultado.pack()
ventana.mainloop() #es el bucle de la ventana

