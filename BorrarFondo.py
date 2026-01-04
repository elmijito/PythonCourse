from rembg import remove
from PIL import Image

removeBG = remove (Image.open('Mijito&Mijita.png'))
removeBG.save("MijitoSinFondo.png")

print("Fondo eliminado con exito")
