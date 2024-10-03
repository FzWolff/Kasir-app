from table_menu import menu_makanan, menu_minuman
def print_table(table_data):
            print("===================================================")
            for row in table_data:
                if len(row) == 3:
                    print(f"| {row[0]:<3} | {row[1]:<30} | {row[2]:<5} |")
                else:
                    print(f"| {row[0]:<3} | {row[1]:<20} | {row[2]:<9} | {row[3]:<5} |")
            print("===================================================")
def menuAdmin():
    print("               <<========================>>               ")
    print("            <<<<   Login Sebagai admin    >>>>            ")
    print("               <<========================>>               ")
    print(" ")
    print(" ")
    print("                     1. Tambah Menu")
    print("                     2. Hapus Menu")
    print("                     3. Lihat Menu")
    print("                     4. Keluar")
    print(" ")
    pilihan2 = input("Masukan Pilihan : ")
    print(" ")
    
    if pilihan2 in ["3"]:
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
            
menuAdmin()
    