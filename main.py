import telebot
from sympy import symbols, solve, Eq

# Tera Asli Token
TOKEN = '8720752639:AAHdgC6XpkV63saRSJ7wfHaWQ0yFIwyI-YU'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Vivek's AI System Online! 😎\n\nBhai, math ka sawal pucho, 'Ratta' nahi logic dikhaunga.")

@bot.message_handler(func=lambda message: True)
def solve_math(message):
    text = message.text.lower()
    
    # Delhi wale ka "Square aur Sum" wala logic
    if "square" in text and "sum" in text:
        try:
            x = symbols('x')
            # Equation: x^2 + x = 30
            equation = Eq(x**2 + x, 30)
            sol = solve(equation, x)
            bot.reply_to(message, f"System logic: x² + x = 30\nSolution: x = {sol}\n\nAb bol bhai, 'System' hang hua ki nahi? 😎")
        except:
            bot.reply_to(message, "Calculation mein thodi dikkat hai, par logic sahi hai!")
    else:
        # Baaki kisi bhi calculation ke liye
        try:
            # ^ ko ** mein badalna taaki Python samajh sake
            safe_text = text.replace('^', '**')
            result = eval(safe_text)
            bot.reply_to(message, f"Result: {result} ✅")
        except:
            bot.reply_to(message, "Bhai, sawal sahi se dalo!")

bot.infinity_polling()
      
