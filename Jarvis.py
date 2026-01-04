import os
from dotenv import load_dotenv # Importante: esto lee el archivo .env que acabas de crear

# Cargar las claves desde el archivo .env
load_dotenv() 

# Leer las variables (Python buscará dentro del archivo .env por ti)
TOKEN = os.getenv("TELEGRAM_TOKEN")
API_KEY = os.getenv("GEMINI_API_KEY")


#Bot de inteligencia artificial

import os
import logging
from dotenv import load_dotenv

# Importamos las librerías de Telegram (La interfaz)
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Importamos la librería de Google Gemini (El Cerebro)
import google.generativeai as genai

# 💡 EXPLICACIÓN: "El logging es nuestra caja negra de avión. 
# Si el bot choca, esto nos dirá por qué."
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# 1. CARGA DE SECRETOS 
# 💡 EXPLICACIÓN: "Aquí cargamos las llaves del archivo .env para no exponerlas."
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
API_KEY = os.getenv("GEMINI_API_KEY")

# 2. CONFIGURACIÓN DE LA IA (CEREBRO) 
# 💡 EXPLICACIÓN: "Le damos la llave a Google para usar su modelo."
genai.configure(api_key=API_KEY)

# 💡 DINÁMICA: "¡Chat! ¿Qué personalidad le ponemos hoy? ¿Sarcástico? ¿Amable?"
# (Modifica este texto en vivo según lo que diga el chat)
SYSTEM_PROMPT = """
Eres JARVIS, un asistente virtual experto en Python.
Tu personalidad es sarcástica y te gusta hacer chistes de programadores.
Usa emojis técnicos como.
Respuestas cortas y directas.
"""

# Configuración del modelo con la personalidad
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash", # Modelo rápido y gratuito
    system_instruction=SYSTEM_PROMPT
)

# 3. MEMORIA DEL BOT (Diccionario) 💾
# 💡 EXPLICACIÓN: "Sin esto, el bot tendría Alzheimer. 
# Guardamos la conversación de cada usuario por separado."
# Estructura: { user_id: chat_session_object }
user_sessions = {}

# --- FUNCIONES DEL BOT ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Comando /start: Se ejecuta cuando alguien inicia el bot.
    """
    user_name = update.effective_user.first_name
    
    # 💡 EXPLICACIÓN: "Saludamos al usuario por su nombre real."
    mensaje_bienvenida = f"¡Hola {user_name}!Soy tu Asistente IA. Pregúntame lo que quieras (si es de código, mejor)."
    
    await update.message.reply_text(mensaje_bienvenida)

async def reset_memory(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Comando /borrar: Reinicia la memoria de la conversación.
    """
    user_id = update.effective_user.id
    
    if user_id in user_sessions:
        del user_sessions[user_id]
        await update.message.reply_text("🧠 ¡Memoria formateada! No recuerdo nada de ti.")
    else:
        await update.message.reply_text("🤨 No teníamos ninguna conversación guardada.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    CEREBRO PRINCIPAL: Recibe texto -> Envía a IA -> Responde en Telegram.
    """
    user_id = update.effective_user.id
    user_text = update.message.text

    # 💡 UX PRO: "Mostramos 'Escribiendo...' para que el usuario sepa que la IA piensa."
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")

    try:
        # 1. Verificar si el usuario ya tiene sesión abierta
        if user_id not in user_sessions:
            # Si es nuevo, iniciamos un chat con historial vacío
            user_sessions[user_id] = model.start_chat(history=[])
        
        chat = user_sessions[user_id]

        # 2. Enviar el mensaje a Gemini
        # 💡 EXPLICACIÓN: "Aquí ocurre la magia. El texto viaja a los servidores de Google."
        response = chat.send_message(user_text)
        
        # 3. Responder al usuario en Telegram
        # .text extrae solo la parte de texto de la respuesta de la IA
        await update.message.reply_text(response.text)

    except Exception as e:
        # 💡 ERROR HANDLING: "Si algo explota, no queremos que el bot muera. Lo atrapamos."
        logging.error(f"Error con la IA: {e}")
        # Si falla (ej: sesión expirada), reiniciamos la sesión
        user_sessions[user_id] = model.start_chat(history=[])
        await update.message.reply_text("😵‍💫 Tuve un glitch en mis circuitos. Intenta preguntar de nuevo.")

# --- ARRANQUE DEL SISTEMA ---

if __name__ == "__main__":
    print("🚀 INICIANDO SISTEMA JARVIS...")
    print("✅ Conectado a Telegram...")

    # Construimos la aplicación
    app = Application.builder().token(TOKEN).build()

    # Agregamos los "Oídos" del bot (Handlers)
    app.add_handler(CommandHandler("start", start))   # Escucha /start
    app.add_handler(CommandHandler("borrar", reset_memory)) # Escucha /borrar
    
    # Escucha cualquier texto que NO sea un comando
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Ejecutar el bot
    print("🔥 BOT ONLINE Y ESPERANDO MENSAJES")
    app.run_polling()