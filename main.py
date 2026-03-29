import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")

users = {}

menu = [
    ["🎮 Iniciar Juego"],
    ["⛏ Minar Oro", "🛒 Comprar Leprechauns"],
    ["🍀 Tus Leprechauns", "💰 Depositar"],
    ["🏦 Retirar", "👥 Referidos"],
    ["❓ Ayuda"]
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = ReplyKeyboardMarkup(menu, resize_keyboard=True)
    await update.message.reply_text(
        "🍀 Dark Leprechaun TON Miner\n\nBienvenido!",
        reply_markup=keyboard
    )

async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    text = update.message.text

    if text == "🎮 Iniciar Juego":
        if user_id not in users:
            users[user_id] = {"gold": 1000}
            await update.message.reply_text("🍀 Bienvenido!\n\nRecibiste 1000 ORO inicial!")
        else:
            await update.message.reply_text("Ya iniciaste el juego!")

    elif text == "⛏ Minar Oro":
        gold = users.get(user_id, {}).get("gold", 0)
        await update.message.reply_text(f"⛏ Oro actual: {gold}")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, menu_handler))

print("Bot iniciado...")
app.run_polling()
