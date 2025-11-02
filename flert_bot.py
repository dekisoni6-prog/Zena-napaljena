
import os
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import random

# Ubaci svoj TOKEN i OpenAI API key preko Environment Variables
TOKEN = os.environ.get("")
OPENAI_API_KEY = os.environ.get("")
openai.api_key = OPENAI_API_KEY

PERSONA_NAME = "ZenaBot"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tekst = f"Hej {update.effective_user.first_name or ''} 😉\nJa sam {PERSONA_NAME}, tvoj flert/šaljivi AI robot 🤖💋"
    await update.message.reply_text(tekst)

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_msg = update.message.text

    prompt = f"Igraj ulogu ženske flert/šaljive AI osobe. Odgovori na poruku: {user_msg}"

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=60,
        temperature=0.9
    )

    reply = response.choices[0].text.strip()
    await update.message.reply_text(reply)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
    print(f"{PERSONA_NAME} je aktivna 💋")
    app.run_polling()

if __name__ == "__main__":
    main()
