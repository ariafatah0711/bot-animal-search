import logging
import os

# Buat logger utama
def init_log(level):
    if not os.path.exists('log'):
        os.makedirs('log')

    logger = logging.getLogger(f'logger_lv{level}')
    
    # Kalau handler sudah ada, langsung return logger
    if logger.hasHandlers():
        return logger
    
    logger.setLevel(logging.DEBUG)

    # Tambahkan file handler ke semua level yang lebih tinggi
    for lvl in range(level, 3):
        file_handler = logging.FileHandler(f'log/log_lv{lvl}.log')
        file_handler.setLevel(logging.DEBUG)
        file_formatter = logging.Formatter('%(asctime)s - %(message)s')
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

    return logger

# Buat console logger unik per level
console_loggers = {}

def init_console(level):
    if level in console_loggers:
        return console_loggers[level]
    
    logger = logging.getLogger(f'console_lv{level}')
    logger.setLevel(logging.DEBUG)

    # Warna sesuai level
    colors = {
        # 0: '\033[1;37m',  # Putih terang
        # 1: '\033[1;34m',  # Biru
        # 2: '\033[1;32m',  # Hijau
        # 3: '\033[1;31m'   # Merah
        0: '\033[1;32m',  # Hijau
        1: '\033[1;37m',  # Putih terang
        2: '\033[1;34m'  # Biru
    }
    
    color = colors.get(level, '\033[1m')
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_formatter = logging.Formatter(f'{color}%(message)s\033[0m')
    console_handler.setFormatter(console_formatter)
    
    logger.addHandler(console_handler)
    console_loggers[level] = logger
    return logger

# Fungsi utama untuk logging tanpa duplikasi
def print_text(text, verbose, level=0):
    # if level > 3: return
    logger = init_log(level)

    # Log ke file sesuai level
    logger.debug(text)

    # Log ke terminal hanya jika verbose >= level
    if verbose >= level:
        console_logger = init_console(level)
        console_logger.debug(text)