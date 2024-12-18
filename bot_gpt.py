Python 3.13.1 (v3.13.1:06714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import os
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Carica le chiavi API dalle variabili di ambiente
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Configura OpenAI
... openai.api_key = OPENAI_API_KEY
... 
... # Funzione per interrogare GPT
... async def chat_with_gpt(update: Update, context: ContextTypes.DEFAULT_TYPE):
...     user_message = update.message.text
...     
...     try:
...         # Chiamata a GPT-4
...         response = openai.Completion.create(
...             model="gpt-4",
...             prompt=user_message,
...             max_tokens=200,
...             temperature=0.7
...         )
...         
...         # Risposta al messaggio
...         reply = response.choices[0].text.strip()
...         await update.message.reply_text(reply)
...     except Exception as e:
...         await update.message.reply_text(f"Errore: {str(e)}")
... 
... # Comando di start
... async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
...     await update.message.reply_text("Ciao! Scrivi una domanda e ti risponderò con GPT-4.")
... 
... # Funzione principale
... def main():
...     app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
...     
...     app.add_handler(CommandHandler("start", start))
...     app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat_with_gpt))
...     
...     print("Bot avviato...")
...     app.run_polling()
... 
... if __name__ == "__main__":
...     main()
