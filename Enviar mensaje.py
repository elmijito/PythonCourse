import pywhatkit
import datetime
import time

# Datos del mensaje
contacto = "+573152506230"  # Número con código de país (CO = +57)
mensaje = "¡Ey! Te amo Jamona😎"
hora_envio = "20:00"  # Formato 24h (hora:minutos)

# Convertimos la hora a enteros
hora, minuto = map(int, hora_envio.split(":"))

# Programamos el mensaje
print(f"Programando mensaje para {contacto} a las {hora}{minuto}...")
pywhatkit.sendwhatmsg(contacto, mensaje, hora, minuto)
