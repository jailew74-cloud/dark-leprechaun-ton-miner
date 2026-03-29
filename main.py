import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")

menu = [
    ["⛏ Mine", "🛒 Shop"],
    ["🏛 Hall", "🏦 Vault"]
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = ReplyKeyboardMarkup(menu, resize_keyboard=True)
    await update.message.reply_text(
        "🍀 Dark Leprechaun TON Miner\n\nBienvenido minero!",
        reply_markup=keyboard
    )

async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "⛏ Mine":
        await update.message.reply_text("⛏ Tus Leprechauns están minando oro...")
        
    elif text == "🛒 Shop":
        await update.message.reply_text("🛒 Tienda de Leprechauns (Próximamente)")
        
    elif text == "🏛 Hall":
        await update.message.reply_text("🏛 Tus Leprechauns (Próximamente)")
        
    elif text == "🏦 Vault":
        await update.message.reply_text("🏦 Tu oro guardado (Próximamente)")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, menu_handler))

print("Bot iniciado...")
app.run_polling()
