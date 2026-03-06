import wmi #Para acceder a información del hardware en Windows.
import re #Para trabajar con expresiones regulares (búsqueda de patrones en texto).

def extraer_modelo_gpu(texto):
    # Extrae el número de modelo más alto de la GPU (ej: RTX 4070 Ti -> 4070)
    numeros = re.findall(r'\d+', texto)
    return max(map(int, numeros)) if numeros else 0

def extraer_modelo_cpu(texto):
    numeros = re.findall(r'\d+', texto)
    return max(map(int, numeros)) if numeros else 0

# ===== DATOS DE TU PC =====
pc = wmi.WMI()
gpu = pc.Win32_VideoController()[0].Caption
cpu = pc.Win32_Processor()[0].Name
ram_gb = int(int(pc.Win32_ComputerSystem()[0].TotalPhysicalMemory) / (1024 ** 3))

# ===== REQUISITOS GTA 6 =====
req_minimos = {
    "GPU": 2060,  # Usamos el número más bajo requerido (RTX 2060)
    "CPU": 3600,  # Ryzen 5 3600 como referencia
    "RAM": 8
}

# ===== EVALUACIÓN =====
modelo_gpu = extraer_modelo_gpu(gpu)
modelo_cpu = extraer_modelo_cpu(cpu)

gpu_ok = modelo_gpu >= req_minimos["GPU"]
cpu_ok = modelo_cpu >= req_minimos["CPU"]
ram_ok = ram_gb >= req_minimos["RAM"]

# ===== RESULTADOS =====
print("=== ANÁLISIS GTA 6 ===")
print(f"GPU: {gpu} → {'' if gpu_ok else '❌'} (Mínimo: RTX 2060/RX 5700)")
print(f"CPU: {cpu} → {'' if cpu_ok else '❌'} (Mínimo: Ryzen 5 3600 / i5-8600)")
print(f"RAM: {ram_gb}GB → {'' if ram_ok else '❌'} (Mínimo: 8GB)")

if all([gpu_ok, cpu_ok, ram_ok]):
    print("\n🎉 ¡Tu PC PUEDE con GTA 6! (Configuración media-alta)")
elif any([gpu_ok, cpu_ok]):
    print("\n⚠️ Jugarás con ajustes (actualiza lo rojo)")
else:
    print("\n❌ Necesitas mejor hardware para GTA 6")

