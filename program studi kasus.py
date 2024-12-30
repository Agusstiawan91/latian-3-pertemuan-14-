import re

# Fungsi untuk memvalidasi nama lengkap (hanya huruf)
def validasi_nama(nama):
    if nama.isalpha():
        return True
    else:
        return False

# Fungsi untuk memvalidasi nomor telepon (hanya angka)
def validasi_telepon(telepon):
    if telepon.isdigit():
        return True
    else:
        return False

# Fungsi untuk memvalidasi email (harus mengandung "@" dan ".")
def validasi_email(email):
    if "@" in email and "." in email:
        return True
    else:
        return False

# Fungsi utama untuk menjalankan validasi
def validasi_pendaftaran(nama, telepon, email):
    valid_nama = validasi_nama(nama)
    valid_telepon = validasi_telepon(telepon)
    valid_email = validasi_email(email)

    # Menampilkan pesan kesalahan jika ada input yang tidak valid
    if valid_nama and valid_telepon and valid_email:
        print("Data pendaftaran valid.")
    else:
        if not valid_nama:
            print("Error: Nama lengkap harus hanya berisi huruf.")
        if not valid_telepon:
            print("Error: Nomor telepon harus hanya berisi angka.")
        if not valid_email:
            print("Error: Email harus mengandung karakter '@' dan '.'.")
    
# Input dari pengguna
nama = input("Masukkan nama lengkap: ")
telepon = input("Masukkan nomor telepon: ")
email = input("Masukkan email: ")

# Panggil fungsi validasi
validasi_pendaftaran(nama, telepon, email)
