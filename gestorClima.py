# Importamos Streamlit para crear la interfaz gráfica
import streamlit as st

# Importamos requests para hacer peticiones HTTP a la API del clima
import requests

# --------------------------------------------------
# CONFIGURACIÓN GENERAL DE LA PÁGINA
# --------------------------------------------------

# Configura el título de la pestaña y el ícono del navegador
st.set_page_config(
    page_title="Clima Aesthetic",
    page_icon="",
    layout="centered"  # Centra el contenido para mejor UX
)

# --------------------------------------------------
# ESTILOS PERSONALIZADOS (CSS)
# --------------------------------------------------

# Inyectamos CSS para un diseño oscuro y moderno
st.markdown(
    """
    <style>
        .stApp {
            background-color: #0e1117;
            color: white;
        }
        div[data-testid="metric-container"] {
            background-color: #262730;
            border-radius: 12px;
            padding: 15px;
            border: 1px solid #4b4b4b;
        }
    </style>
    """,
    unsafe_allow_html=True  # Permitimos HTML/CSS dentro de Streamlit
)

# --------------------------------------------------
# TÍTULO Y DESCRIPCIÓN
# --------------------------------------------------

# Título principal de la aplicación
st.title("Dashboard del Clima")

# Texto descriptivo debajo del título
st.write("Consulta el clima actual de tu ciudad favorita en tiempo real")

# --------------------------------------------------
# DATOS BASE (CIUDADES)
# --------------------------------------------------

# Diccionario con ciudades y sus coordenadas geográficas
ciudades = {
    "Bogotá": {"lat": 4.60, "lon": -74.08},
    "Ciudad de México": {"lat": 19.43, "lon": -99.13},
    "Buenos Aires": {"lat": -34.60, "lon": -58.38},
    "Madrid": {"lat": 40.41, "lon": -3.70},
    "Tokyo": {"lat": 35.67, "lon": 139.65}
}

# --------------------------------------------------
# FUNCIÓN PARA OBTENER EL CLIMA (OPTIMIZADA)
# --------------------------------------------------

# Cacheamos la función para evitar llamadas repetidas a la API
@st.cache_data(ttl=600)  # Cache por 10 minutos
def obtener_clima(lat, lon):
    """
    Obtiene el clima actual desde Open-Meteo
    """
    # Construimos la URL de la API con coordenadas
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}&current_weather=true"
    )

    # Hacemos la petición HTTP
    response = requests.get(url, timeout=10)

    # Verificamos que la respuesta sea correcta
    response.raise_for_status()

    # Retornamos los datos convertidos a JSON
    return response.json()

# --------------------------------------------------
# INTERFAZ DE USUARIO
# --------------------------------------------------

# Creamos un menú desplegable con las ciudades disponibles
ciudad_elegida = st.selectbox(
    "Selecciona una ciudad:",
    list(ciudades.keys())
)

# Botón que dispara la consulta del clima
if st.button("Obtener Clima"):

    try:
        # Extraemos latitud y longitud de la ciudad elegida
        lat = ciudades[ciudad_elegida]["lat"]
        lon = ciudades[ciudad_elegida]["lon"]

        # Llamamos a la función que obtiene el clima
        datos = obtener_clima(lat, lon)

        # Extraemos temperatura y velocidad del viento
        temperatura = datos["current_weather"]["temperature"]
        viento = datos["current_weather"]["windspeed"]

        # Creamos columnas para mostrar métricas
        col1, col2, col3 = st.columns(3)

        # Mostramos la temperatura
        col1.metric(
            label="Temperatura",
            value=f"{temperatura} °C"
        )

        # Mostramos la velocidad del viento
        col2.metric(
            label="Viento",
            value=f"{viento} km/h"
        )

        # Métrica estética / divertida
        col3.metric(
            label="✨ Mood del Clima",
            value="Aesthetic"
        )

        # Mensaje de éxito
        st.success(f"Clima actualizado para {ciudad_elegida}")

        # Animación visual porque somos felices
        st.balloons()

    except requests.exceptions.RequestException:
        # Error relacionado con conexión o API
        st.error("No se pudo conectar con el servicio del clima ")

    except KeyError:
        # Error si la estructura del JSON cambia
        st.error("Error inesperado al procesar los datos ")
