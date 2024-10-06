from table_menu import menu_makanan, menu_minuman
from tambah_menu import tambah_menu, print_table  # Import fungsi dari tambah_menu.py

def menuAdmin():
    print("               <<========================>>               ")
    print("            <<<<   Login Sebagai admin    >>>>            ")
    print("               <<========================>>               ")
    print("                                                          ")
    print("                     1. Tambah Menu")
    print("                     2. Hapus Menu")
    print("                     3. Lihat Menu")
    print("                     4. Keluar")
    print(" ")
    pilihan2 = input("Masukan Pilihan : ")
    print(" ")
    
    if pilihan2 == "1":
        print("Tambah Menu ke:")
        print("1. Makanan")
        print("2. Minuman")
        pilihan_menu = input("Pilih menu yang ingin ditambah: ")

        if pilihan_menu == "1":
            tambah_menu(menu_makanan)
        elif pilihan_menu == "2":
            tambah_menu(menu_minuman)
        else:
            print("Pilihan tidak valid!")
        
        menuAdmin()

    elif pilihan2 == "2":
        print("Fitur Hapus Menu")
        # Logika hapus menu
        menuAdmin()

    elif pilihan2 == "3":
        print("Tabel Makanan:")
        print_table(menu_makanan)

        pilihan3 = input("Lanjut Menu Minuman (Y/N) : ")

        if pilihan3 in ["Y", "y"]:
            print("Tabel Minuman:")
            print_table(menu_minuman)
            input("Kembali (Enter) : ")
            menuAdmin()
        elif pilihan3 in ["N", "n"]:
            menuAdmin()

    elif pilihan2 == "4":
        print("Kembali ke login...")
        from Kasir import login  # Mengimpor login hanya ketika dibutuhkan
        login()  # Kembali ke fungsi login
