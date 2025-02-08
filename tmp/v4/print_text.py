import logging, os

# Fungsi untuk menginisialisasi logging dengan file dan level tertentu
def init_logger(level):
    # Membuat folder 'log' jika belum ada
    if not os.path.exists('log'):
        os.makedirs('log')

    # Inisialisasi logger
    logger = logging.getLogger(f'logger_lv{level}')
    logger.setLevel(logging.DEBUG)

    # Cek apakah handler sudah ada, jika belum, tambahkan handler konsol dan file
    if not logger.handlers:  # Mengecek jika logger sudah memiliki handler
        # File handler untuk setiap level di dalam folder log
        file_handler = logging.FileHandler(f'log/log_lv{level}.log')
        file_handler.setLevel(logging.DEBUG)
        file_formatter = logging.Formatter('%(asctime)s - %(message)s')
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

        # Console handler untuk menampilkan di konsol dengan warna
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        if level == 0:
            console_formatter = logging.Formatter('\033[1;32m %(message)s \033[0m')  # Format sederhana untuk console
        else:
            console_formatter = logging.Formatter('\033[1m %(message)s \033[0m')  # Format sederhana untuk console
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)
    
    return logger

def print_text(text, verbose, level=0):
    if verbose >= level:
        # print(f"\033[1m{text}\033[0m")s
        
        logger = init_logger(level)
        logger.debug(f"{text}")