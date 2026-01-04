import os
import shutil


descargas = os.path.expanduser("~/Downloads")

tipos = {
    "Imagenes": [".png", ".jpg", ".jpeg", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi"],
    "ZIPs": [".zip", ".rar"],
    "Instaladores": [".exe", ".dmg", ".pkg"],
}

for archivo in os.listdir(descargas):
    ruta_archivo = os.path.join(descargas, archivo)
    if os.path.isfile(ruta_archivo):
        _, ext = os.path.splitext(archivo)

        for carpeta, extensiones in tipos.items():
            if ext.lower() in extensiones:
                destino = os.path.join(descargas, carpeta)
                os.makedirs(destino, exist_ok=True)
                shutil.move(ruta_archivo, os.path.join(destino, archivo))
                break  

