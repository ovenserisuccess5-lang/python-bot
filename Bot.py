import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters
from urllib.parse import quote

TOKEN = "  "
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send me a prompt and I'll generate an image.")

async def generate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = update.message.text

    image_url = f"https://image.pollinations.ai/prompt/{quote(prompt)}"

    await update.message.reply_photo(photo=image_url)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, generate))

print("Bot is Running...")
app.run_polling()
