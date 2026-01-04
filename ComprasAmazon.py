#https://www.amazon.com/s?k=

import webbrowser
import speech_recognition as sr #importamos la libreria de reconocimiento de voz
import pyttsx3 #importamos la librería de texto a voz

reconizer = sr.Recognizer() #creamos un objeto de reconocimiento de voz
engine = pyttsx3.init() #inicializamos el motor de texto a voz

def hablar():
    microfono = sr.Microphone() #creamos un objeto de micrófono
    with microfono as source:

        audio = reconizer.listen(source) #escuchamos el audio del micrófono
    text = reconizer.recognize_google(audio, language='es-ES') #reconocemos el audio y lo convertimos a texto

    print(f'tu dijiste: {text}') #imprimimos el texto reconocido
    return text.lower() #convertimos el texto a minúsculas y lo devolvemos

if 'amazon' in hablar():
    engine.say('Hola, ¿Que quieres comprar?')  #si el texto contiene 'amazon', respondemos con un saludo
    engine.runAndWait() 
    text = hablar() 
    webbrowser.open(f'https://www.amazon.com/s?k={text}')