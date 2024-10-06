from table_menu import menu_makanan, menu_minuman

def print_table(table_data):
    print("===================================================")
    for row in table_data:
        if len(row) == 3:
            print(f"| {row[0]:<3} | {row[1]:<30} | {row[2]:<5} |")
        else:
            print(f"| {row[0]:<3} | {row[1]:<20} | {row[2]:<9} | {row[3]:<5} |")
    print("===================================================")

def tambah_menu(menu):
    print("Tambah Menu:")
    nama = input("Masukkan Nama Menu: ")
    harga = input("Masukkan Harga: ")

    if menu == menu_makanan:
        level = input("Masukkan Level (contoh: Level 1-4): ")
        nomor = len(menu)  # Menghitung nomor menu berdasarkan panjang list
        menu.append([str(nomor), nama, level, harga])
    elif menu == menu_minuman:
        nomor = len(menu)  # Menghitung nomor menu berdasarkan panjang list
        menu.append([str(nomor), nama, harga])

    print("Menu berhasil ditambahkan!")
