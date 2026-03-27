import tkinter as tk 
import random

# Diccionario con preguntas y respuestas
trivia = {
    "¿Cuál es la capital de Francia?": {
        "opciones": ["París", "Madrid", "Berlín", "Londres"],
        "respuesta": "París"
    },
    "¿Qué lenguaje se usa para ciencia de datos?": {
        "opciones": ["Python", "HTML", "CSS", "JavaScript"],
        "respuesta": "Python"
    },
    "¿Qué animal es el rey de la selva?": {
        "opciones": ["León", "Tigre", "Elefante", "Jirafa"],
        "respuesta": "León"
    },
    "¿Qué planeta es el más cercano al sol?": {
        "opciones": ["Mercurio", "Venus", "Tierra", "Marte"],
        "respuesta": "Mercurio"
    },
}

preguntas_ya_usadas = set()
puntuacion = 0

#configuraci+on la interfaz grafica GUI
root = tk.Tk()
root.title("Trivia de Conocimientos Generales para mijitos")
root.geometry("500x400")

pregunta_label = tk.Label(root, text="", wraplength=300, font=("Arial", 14))
pregunta_label.pack(pady=20)

botones_opciones = []

def mostrar_pregunta():
    global pregunta_actual
    if len(preguntas_ya_usadas) == len (trivia):
        pregunta_label.config(text=f"Fin del juego! Tu puntaje: {puntuacion}")
        for boton in botones_opciones:
            boton.pack_forget()
        return

    pregunta_actual = random.choice(list(set(trivia.keys()) - preguntas_ya_usadas))
    preguntas_ya_usadas.add(pregunta_actual)
    opciones = trivia[pregunta_actual]["opciones"]

    pregunta_label.config(text=pregunta_actual)

    for i in range(4):
        botones_opciones[i].config(text=opciones[i], command = lambda o = opciones[i]:  verificar_respuesta(o))
    
def verificar_respuesta (seleccion):
    global puntuacion
    if seleccion == trivia[pregunta_actual]["respuesta"]:
        puntuacion += 1
    mostrar_pregunta()

#crear los botones de las opciones
for _ in range(4):
    boton = tk.Button(root, text="", font=("Arial", 12), width=20)
    boton.pack(pady=5)
    botones_opciones.append(boton)

mostrar_pregunta()
root.mainloop()

                               



