import os, telebot
from dotenv import load_dotenv
from data import DataLoader
import app as app
import state_user

if __name__ == '__main__':
    args = app.getArgument(); v = args.verbose
    valid_modes = ['kmp', 'boyer_more']

    load_dotenv('.env')
    BOT_TOKEN = os.environ.get('BOT_TOKEN')
    bot = telebot.TeleBot(str(BOT_TOKEN))

    user_states = state_user.load_state()

    '''animal_local'''
    # file = 'data.xlsx'    
    # pattern_1 = ['pattern', 'value', 'priority']
    # pattern_2 = ['name', 'description']
    # valid_modes = ['kmp', 'boyer_more']

    # df_animals = DataLoader(file, pattern_1).load_data(sort=True)
    # df_describe = DataLoader(file, pattern_2, 'Sheet2').load_data()

    '''pentest_local'''
    # file = 'data_dump.xlsx'
    # pattern_1 = ['pattern', 'solusi', 'prioritas']
    
    # df_animals = DataLoader(file, pattern_1).load_data(sort=True)
    
    '''pentest_search'''
    file = 'data_dump.xlsx'
    pattern_list = DataLoader(file, ['pattern'], 'Sheet2').load_data()
    pattern_list_value = DataLoader(file, ['solusi'], 'Sheet2').load_data()
    
    # app.search_pattern_with('aku inngin mengatasi serangan dos', pattern_list_value, pattern_list)
    # app.search_pattern_with('menjaga https agar maan dari serangan dos atau ddos', pattern_list_value, pattern_list)
    # result = app.search_pattern_with('menjaga https agar aman', pattern_list_value, pattern_list)
    # print(result)
    # app.search_pattern_with('aku inngin mengatasi serangan dos', pattern_list_value, pattern_list)
    # app.search_pattern_with('aku inngin mengatasi serangan dos', pattern_list_value, pattern_list)
    

    # print(pattern_list)
    # print(pattern_list_value)
    
    # app.print_text(df_animals, v, 3)
    # app.print_text(df_describe, v, 3)
    
    '''/start dan /help'''
    @bot.message_handler(commands=['start', 'help'])
    def start_and_help(message):
        try:
            # Pesan dasar
            response_message = (
                "Gunakan perintah berikut untuk mulai:\n"
                "/search <teks> - Cari pola teks pada data hewan\n"
                "/describe <nama hewan> - Lihat informasi tentang hewan\n"
                "/use <mode> - Pilih mode pencarian (kmp atau boyer_more)\n"
                "/get - Tampilkan mode pencarian Anda saat ini\n"
                "/help - Tampilkan daftar perintah ini"
            )
            
            # Tambahkan pesan selamat datang jika perintahnya /start
            if message.text.startswith('/start'):
                response_message = (
                    "Selamat datang di bot pencarian hewan! 🐾\n\n"
                    + response_message
                )
            
            bot.reply_to(message, response_message)
        except Exception as e:
            bot.reply_to(message, f'Terjadi kesalahan: {str(e)}')

    '''/search'''
    @bot.message_handler(commands=['search'])
    def search(message):
        try:
            command = message.text[8:]
            app.print_text(f'{message.from_user.id} : {message.text}', v, 0)

            if (len(command) < 1):
                bot.reply_to(message, f'masukan teks yang ingin dicari\nex: /search hewan berkaki 4')
                return

            mode = user_states.get(str(message.from_user.id), "boyer_more")
            # result = app.search_pattern(command, df_animals, mode, pattern_1)
            result = app.search_pattern_with(command, pattern_list_value, pattern_list)
            # bot.reply_to(message, str(result))

            result_format = '\n'.join([f"- {item}" for item in result.split(', ')]) + '\n'
            bot.reply_to(message, result_format)
        except Exception as e:
            bot.reply_to(message, f'Terjadi kesalahan: {str(e)}')
    
    '''/describe'''
    # @bot.message_handler(commands=['describe'])
    # def describe(message):
    #     try:
    #         command = message.text[10:]
    #         app.print_text(f'{message.from_user.id} : {message.text}', v, 0)
            
    #         if (len(command) < 1):
    #             bot.reply_to(message, f'masukan nama hewan yang ingin di lihat informasinya\nex: /describe ayam\nex: /describe sapi, kucing')
    #             return

    #         match = []
    #         items = command.split(',')

    #         for item in items:
    #             result = app.describe(item, df_describe)
    #             match.append(result)

    #         bot.reply_to(message, str('\n\n'.join(match)))
    #     except Exception as e:
    #         bot.reply_to(message, f'Terjadi kesalahan: {str(e)}')
    
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
            state = state = user_states.get(str(message.from_user.id), valid_modes[1])

            if state is None:
                 bot.reply_to(message, 'Anda belum memiliki state yang disimpan.')
            else:
                bot.reply_to(message, f'State Anda saat ini: {state}')
        except Exception as e:
            bot.reply_to(message, f'Terjadi kesalahan: {str(e)}')

    bot.infinity_polling()