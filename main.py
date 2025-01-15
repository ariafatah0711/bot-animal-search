import os
from dotenv import load_dotenv
import telebot
import CRUID as CRUID

if __name__ == "__main__":
    load_dotenv('.env')
    BOT_TOKEN = os.environ.get('BOT_TOKEN')
    bot = telebot.TeleBot(str(BOT_TOKEN))

    df = CRUID.load_data()
    
    @bot.message_handler(commands=['search'])
    def search(message):
        try:
            command = message.text[8:]
            if (len(command) < 1):
                bot.reply_to(message, f"masukan teks yang ingin dicari\nex: /search hewan berkaki 4")
                return
            result = CRUID.search_animals(command, df)
            bot.reply_to(message, str(result))
        except Exception as e:
            bot.reply_to(message, f"Terjadi kesalahan: {str(e)}")

    bot.infinity_polling()
