#Raka Emillul Fata
#Praktikum 13

import os

NAMA_FILE = "data.txt"


#Membaca File
def baca_file():
    data = {}

    try:
        with open(NAMA_FILE, "r") as file:
            for baris in file:
                baris = baris.strip()

                if baris == "":
                    continue

                try:
                    nim, nilai = baris.split(",")
                    data[nim] = float(nilai)

                except ValueError:
                    print(f"Data tidak valid diabaikan: {baris}")

    except FileNotFoundError:
        print("File belum ada. Data baru akan dibuat.")

    except Exception as e:
        print("Terjadi kesalahan saat membaca file.")
        print(e)

    return data


#Menyimpan Data
def simpan_data(data):
    try:
        with open(NAMA_FILE, "w") as file:
            for nim, nilai in data.items():
                file.write(f"{nim},{nilai}\n")

        print("\nData berhasil disimpan.")
        print("Lokasi file :", os.path.abspath(NAMA_FILE))

    except Exception as e:
        print("Gagal menyimpan data.")
        print(e)


#Tambah Data
def tambah_data(data):
    nim = input("Masukkan NIM : ").strip()

    if nim == "":
        print("NIM tidak boleh kosong!")
        return

    if not nim.isdigit():
        print("NIM hanya boleh berisi angka!")
        return

    if nim in data:
        print("NIM sudah terdaftar!")
        return

    try:
        nilai = float(input("Masukkan Nilai : "))
        data[nim] = nilai
        print("Data berhasil ditambahkan.")

    except ValueError:
        print("Nilai harus berupa angka!")


#Hapus Data
def hapus_data(data):

    if len(data) == 0:
        print("Belum ada data.")
        return

    nim = input("Masukkan NIM yang akan dihapus : ").strip()

    if nim == "":
        print("NIM tidak boleh kosong!")
        return

    if not nim.isdigit():
        print("NIM hanya boleh berisi angka!")
        return

    if nim in data:
        del data[nim]
        print("Data berhasil dihapus.")
    else:
        print("Data tidak ditemukan.")


#Tampilkan Data
def tampilkan_data(data):

    if len(data) == 0:
        print("Belum ada data.")
        return

    print("\n===== DATA MAHASISWA =====")

    for nim, nilai in data.items():
        print(f"NIM   : {nim}")
        print(f"Nilai : {nilai}")
        print("-" * 25)


#Insertion Sort
def sorting_nilai(data):

    if len(data) == 0:
        print("Belum ada data untuk diurutkan.")
        return

    items = list(data.items())

    for i in range(1, len(items)):
        key = items[i]
        j = i - 1

        while j >= 0 and items[j][1] > key[1]:
            items[j + 1] = items[j]
            j -= 1

        items[j + 1] = key

    print("\n===== DATA TERURUT BERDASARKAN NILAI =====")

    for nim, nilai in items:
        print(f"{nim} : {nilai}")


#Dictionary Search
def cari_data(data):

    if len(data) == 0:
        print("Belum ada data.")
        return

    nim = input("Masukkan NIM yang dicari : ").strip()

    if nim == "":
        print("NIM tidak boleh kosong!")
        return

    if not nim.isdigit():
        print("NIM hanya boleh berisi angka!")
        return

    if nim in data:
        print(f"Nilai mahasiswa {nim} : {data[nim]}")
    else:
        print("Data tidak ditemukan.")


#Menu
def tampilkan_menu():
    print("\n===== MINI PROJECT NILAI MAHASISWA =====")
    print("1. Tambah Data")
    print("2. Hapus Data")
    print("3. Tampilkan Data")
    print("4. Sorting Nilai")
    print("5. Cari Data")
    print("6. Simpan dan Keluar")


#Main Program
def main():

    data = baca_file()

    while True:

        tampilkan_menu()

        pilih = input("Pilih Menu : ").strip()

        if pilih == "1":
            tambah_data(data)

        elif pilih == "2":
            hapus_data(data)

        elif pilih == "3":
            tampilkan_data(data)

        elif pilih == "4":
            sorting_nilai(data)

        elif pilih == "5":
            cari_data(data)

        elif pilih == "6":
            simpan_data(data)
            print("Program selesai.")
            break

        else:
            print("Pilihan menu tidak valid.")

#Menjalankan Program
main()