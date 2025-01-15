import os
from dotenv import load_dotenv
import telebot

from data import DataLoader
import app as app

if __name__ == "__main__":
    load_dotenv('.env')
    BOT_TOKEN = os.environ.get('BOT_TOKEN')
    bot = telebot.TeleBot(str(BOT_TOKEN))

    file = 'data.xlsx'    
    pattern_1 = ['pattern', 'value', 'priority']
    pattern_2 = ['name', 'description']
        
    df_animals = DataLoader(file, pattern_1).load_data(sort=True)
    df_describe = DataLoader(file, pattern_2, 'Sheet2').load_data()

    # print(df_animals)
    # print(df_describe)

    '''/search'''
    @bot.message_handler(commands=['search'])
    def search(message):
        try:
            command = message.text[8:]
            if (len(command) < 1):
                bot.reply_to(message, f"masukan teks yang ingin dicari\nex: /search hewan berkaki 4")
                return
            result = app.search_pattern(command, df_animals)
            bot.reply_to(message, str(result))
        except Exception as e:
            bot.reply_to(message, f"Terjadi kesalahan: {str(e)}")
    
    '''/describe'''
    @bot.message_handler(commands=['describe'])
    def describe(message):
        try:
            command = message.text[10:]
            if (len(command) < 1):
                bot.reply_to(message, f"masukan nama hewan yang ingin di lihat informasinya\nex: /describe ayam\nex: /describe sapi, kucing")
                return

            '''1'''
            # result = app.describe(command, df_describe)
            # bot.reply_to(message, str(result))
            
            '''2'''
            match = []
            items = command.split(',')

            for item in items:
                result = app.describe(item, df_describe)
                match.append(result)

            bot.reply_to(message, str("\n\n".join(match)))
        except Exception as e:
            bot.reply_to(message, f"Terjadi kesalahan: {str(e)}")

    bot.infinity_polling()
