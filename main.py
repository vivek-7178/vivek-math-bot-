import telebot
import google.generativeai as genai
import os

# Render ke Environment Variables se keys uthana
BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
GEMINI_KEY = os.environ.get('GEMINI_API_KEY')

# AI aur Bot setup
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
bot = telebot.TeleBot(BOT_TOKEN)

# Jab koi /start likhe
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Vivek's AI System Online! 😎\nMain Maths solve kar sakta hoon aur aapse baatein bhi kar sakta hoon. Pucho kya puchna hai?")

# Saare messages ka reply AI se dilwana
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    try:
        # AI se jawab mangna
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "Opps! Kuch gadbad ho gayi. Shayad API key ya Network ka chakkar hai.")

# Bot ko chalu rakhna
print("Bot is running...")
bot.infinity_polling()





