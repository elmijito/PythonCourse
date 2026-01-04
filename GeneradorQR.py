#instalación de librería para generar código QR
# -- pip install qrcode en powershell

import qrcode #importar la librería 

#URL - Direccionar el código QR 
twitch_url = "https://www.twitch.tv/elmijito_"

#crear objeto QR
qr = qrcode.QRCode (
    version = 1, # tamaño (1 es pequeño, podría incrementarse para más datos)
    error_correction = qrcode.constants.ERROR_CORRECT_H,#mejore la corrección
    box_size = 10, #tamaño del QR
    border = 4, # grosor de borde
)

# Agregar datos
qr.add_data (twitch_url)
qr.make (fit=True)

#generar la imagen

img = qr.make_image (fill_color = "purple", back_color = "white")

#guardar el código QR
img.save("qr_twitch.png")
print("Código QR generó: qr_twitch.png")

