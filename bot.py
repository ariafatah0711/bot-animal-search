import os
from dotenv import load_dotenv
import telebot
import pandas as pd
from boyer_more import boyer_more

# token
load_dotenv('.env')
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(str(BOT_TOKEN))

# test
# ===========================================================================
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Halo! Ketik /help untuk melihat daftar perintah.")

@bot.message_handler(commands=['echo'])
def echo(message):
    command = message.text[6:]
    # command = message.text.split()[1:]
    if (len(command) < 1):
        bot.reply_to(message, f"masukan teks yang ingin ditampilkan\nex: /echo hello world")
        return
    bot.reply_to(message, command)
# ===========================================================================

# data
file = "data-animals.xlsx"
row = ["pattern", "value", "priority"]
# df = pd.read_excel(file, usecols=row) # default
df = pd.read_excel(file, usecols=row).sort_values(row[2]).reset_index(drop=True) # sort value by priority and reset index

def search_animals(text):
    print(f"[*] text \t: {text}")
    patterns, match, match_same = [], [], []
    
    for index, row in df.iterrows():
        pattern = row['pattern']
        position = boyer_more(text.lower(), pattern.lower())
        if (position != -1):
            value = row["value"]
            if pattern not in patterns:
                patterns.append(pattern)
            if value in match:
                match_same.append(value)
            else:
                match.append(value)

    if (len(match_same) != 0):
        # print(f"[+] value yang sama ditemukan!")
        print(f"    pattern \t: {', '.join(patterns)}")
        print(f"    value \t: {', '.join(match_same)} \n")
        return ', '.join(match_same)
    else:
        # print(f"[+] value yang sama tidak ditemukan!")
        print(f"    pattern \t: {', '.join(patterns)}")
        print(f"    value \t: {', '.join(match)} \n")
        if (len(match) != 0):
            return ', '.join(match)
        return "hewan tidak ditemukan"

# bot
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = """
    Available commands:
    /echo [text] - Echo the provided text.
    /search [text] - Search Animals with string
    """
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['search'])
def search(message):
    try:
        command = message.text[8:]
        if (len(command) < 1):
            bot.reply_to(message, f"masukan teks yang ingin dicari\nex: /search hewan berkaki 4")
            return
        result = search_animals(command)
        bot.reply_to(message, str(result))
    except Exception as e:
        bot.reply_to(message, f"Terjadi kesalahan: {str(e)}")

bot.infinity_polling()
