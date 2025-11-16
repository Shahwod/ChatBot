import telebot
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
TELEGRAM_TOKEN = os.getenv("7863029490:AAG5gAVciJzB1Uptoh8XEVMHAmdPUyqFFFA")
VERTEX_API_KEY = os.getenv("AIzaSyCBCm0AMHmMXmICJoev5Vq2fJ2AByBHy4U")

genai.configure(api_key=AIzaSyCBCm0AMHmMXmICJoev5Vq2fJ2AByBHy4U)
model = genai.GenerativeModel("gemini-1.5-flash")

bot = telebot.TeleBot(7863029490:AAG5gAVciJzB1Uptoh8XEVMHAmdPUyqFFFA)

chat_history = {}

@bot.message_handler(func=lambda m: True)
def handle(message):
    cid = message.chat.id
    if cid not in chat_history:
        chat_history[cid] = []

    chat_history[cid].append({"role": "user", "content": message.text})

    try:
        ctx = chat_history[cid][-10:]
        prompt = "\n".join([x["content"] for x in ctx])

        reply = model.generate_content(prompt)
        bot.reply_to(message, reply.text)

        chat_history[cid].append({"role": "assistant", "content": reply.text})
    except Exception as e:
        bot.reply_to(message, f"Ошибка: {e}")

bot.polling(none_stop=True)
