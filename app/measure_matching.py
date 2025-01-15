import time
from . import matching  # Asumsi matching adalah fungsi pencocokan yang sudah Anda definisikan

def measure_matching_speed(text, pattern):
    matchs = []  # Menyimpan hasil yang sudah ditemukan
    # Mulai waktu eksekusi
    start_time = time.time()
    
    # Jalankan fungsi matching
    position = matching(text, pattern)
    
    # Jika posisi tidak ditemukan, langsung return dan tidak lanjut
    if position == -1:
        print("Pattern tidak ditemukan.")
        return None, 0  # Return jika tidak ditemukan
    
    # Cek apakah posisi sudah ditemukan sebelumnya
    if position in matchs:
        print("Pattern sudah ditemukan sebelumnya.")
        return None, 0  # Return jika sudah ditemukan

    # Menambahkan posisi yang ditemukan ke dalam list
    matchs.append(position)
    
    # Menghitung waktu selesai setelah matching
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    # Output hasil
    print(f"Pattern ditemukan pada posisi: {position}")
    print(f"Waktu eksekusi: {elapsed_time:.8f} detik")
    
    # Return hanya sekali setelah semua proses selesai
    return position, elapsed_time