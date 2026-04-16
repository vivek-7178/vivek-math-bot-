import telebot
import google.generativeai as genai
import os

# Render ke variables se keys uthana
BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
GEMINI_KEY = os.environ. get('GEMINI_API_KEY')

# AI aur Bot setup
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-pro')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Vivek's AI Online! 😎\nAb main Maths, English aur duniya ka har sawal samajhta hoon. Pucho!")

@bot.message_handler(func=lambda message: True)
def chat(message):
    try:
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "Bhai, Render par Keys check karo!")

bot.infinity_polling()


