import csv
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- CONFIGURACIÓN DE RUTA AUTOMÁTICA ---
# Esto detecta tu usuario solo, sin importar si es 'aleja' u otro
ruta_escritorio = os.path.join(os.path.expanduser("~"), "Desktop")
nombre_archivo = 'estudio_mercado_tecnologia.csv'
ruta_completa = os.path.join(ruta_escritorio, nombre_archivo)

# --- CONFIGURACIÓN DEL NAVEGADOR (MODO ANTI-DETECCIÓN) ---
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-blink-features=AutomationControlled') # Oculta que es un bot
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Truco extra: Cambiar el User Agent para parecer un humano
driver.execute_cdp_cmd('Network.setUserAgentOverride', {
    "userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
})

url = 'https://listado.mercadolibre.com.co/componentes-pc'

try:
    print(f"Abriendo navegador en: {url}...")
    driver.get(url)

    # Espera un poco para que el JS se ejecute bien
    time.sleep(5)

    # Buscar los productos
    WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'ui-search-result__content'))
    )

    productos_html = driver.find_elements(By.CLASS_NAME, 'ui-search-result__content')
    lista_datos = []

    print(f"Extrayendo {len(productos_html)} productos...")

    for item in productos_html:
        try:
            nombre = item.find_element(By.CLASS_NAME, 'ui-search-item__title').text
            # Intentar capturar el precio con un selector más genérico por si cambió
            precio_texto = item.find_element(By.CSS_SELECTOR, '.andes-money-amount__fraction').text
            precio_limpio = precio_texto.replace('.', '').replace(',', '')
            lista_datos.append([nombre, precio_limpio])
        except:
            continue

    # Guardar archivo
    with open(ruta_completa, 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerow(['Producto', 'Precio_COP'])
        writer.writerows(lista_datos)

    print(f"\n¡EXITO! Archivo creado en: {ruta_completa}")
    os.startfile(ruta_escritorio)

except Exception as e:
    print(f"Error específico: {e}")

finally:
    time.sleep(2)
    driver.quit()