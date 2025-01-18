import os
from dotenv import load_dotenv
import telebot

from data import DataLoader
import app as app
import state_user

if __name__ == '__main__':
    load_dotenv('.env')
    BOT_TOKEN = os.environ.get('BOT_TOKEN')
    bot = telebot.TeleBot(str(BOT_TOKEN))

    user_states = state_user.load_state()

    # animal_local
    file = 'data.xlsx'    
    pattern_1 = ['pattern', 'value', 'priority']
    pattern_2 = ['name', 'description']
    valid_modes = ['kmp', 'boyer_more']

    df_animals = DataLoader(file, pattern_1).load_data(sort=True)
    df_describe = DataLoader(file, pattern_2, 'Sheet2').load_data()

    # animal_drive

    '''/search'''
    @bot.message_handler(commands=['search'])
    def search(message):
        try:
            command = message.text[8:]
            if (len(command) < 1):
                bot.reply_to(message, f'masukan teks yang ingin dicari\nex: /search hewan berkaki 4')
                return

            mode = user_states.get(str(message.from_user.id), "boyer_more")
            result = app.search_pattern(command, df_animals, mode)
            bot.reply_to(message, str(result))
        except Exception as e:
            bot.reply_to(message, f'Terjadi kesalahan: {str(e)}')
    
    '''/describe'''
    @bot.message_handler(commands=['describe'])
    def describe(message):
        try:
            command = message.text[10:]
            if (len(command) < 1):
                bot.reply_to(message, f'masukan nama hewan yang ingin di lihat informasinya\nex: /describe ayam\nex: /describe sapi, kucing')
                return

            match = []
            items = command.split(',')

            for item in items:
                result = app.describe(item, df_describe)
                match.append(result)

            bot.reply_to(message, str('\n\n'.join(match)))
        except Exception as e:
            bot.reply_to(message, f'Terjadi kesalahan: {str(e)}')
    
    '''/use'''
    @bot.message_handler(commands=['use'])
    def use(message):
        try:
            args = message.text.split()

            if len(args) < 2:
                bot.reply_to(message, 'Harap berikan mode yang valid setelah perintah /use. Contoh: /use kmp')

            mode_value = args[1]

            user_id = str(message.from_user.id)
            state_id = user_states[user_id] = mode_value

            save_status = state_user.save_state(user_id, state_id, valid_modes)

            if save_status == 0:
                bot.reply_to(message, f"Mode tidak valid. Pilih salah satu mode berikut: {', '.join(valid_modes)}")
            else:
                bot.reply_to(message, f'Mode Anda telah berhasil disimpan: {mode_value}')

        except Exception as e:
            bot.reply_to(message, f'Terjadi kesalahan: {str(e)}')
    
    '''/get'''
    @bot.message_handler(commands=['get'])
    def get(message):
        try:
            state = state = user_states.get(str(message.from_user.id), None)

            if state is None:
                 bot.reply_to(message, 'Anda belum memiliki state yang disimpan.')
            else:
                bot.reply_to(message, f'State Anda saat ini: {state}')
        except Exception as e:
            bot.reply_to(message, f'Terjadi kesalahan: {str(e)}')

    bot.infinity_polling()