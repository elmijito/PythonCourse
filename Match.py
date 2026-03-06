def bot_comando(comando):
   
    match comando.lower().split():  #limpiamos el texto para ingresar los comandos
              
        case ["hola"]: #Para el caso 1: Comandos con simples palabras
            #Si la lista tiene exactamente el comando o la palabra "hola" entonces devolverá el valor del return
            return "¡Hey! ¿Qué tal, dev? "
            #Si la lista tiene exactamente el comando o la palabra "ayuda" entonces devolverá el valor del return    
        case ["ayuda"]:
            # Patrones de captura de variables
            return "Comandos: hola, sumar [a] [b], salir"

            # caso 3 python verifica 3 elementos 
        case ["sumar", num1, num2]:

            try:
                suma = int(num1) + int(num2)
                return f"La suma es: {suma}"
            except ValueError:
                return "Bro, necesito números, no letras"


        case _:
            return "No entendí nada. Intenta de nuevo "

# --- ZONA DE PRUEBAS (Para correr en consola) ---
print(bot_comando("Hola"))           # Salida: ¡Hey! ¿Qué tal, dev? 
print(bot_comando("sumar 10 5"))     # Salida: La suma es: 15 
print(bot_comando("bailar"))         # Salida: No entendí nada...

