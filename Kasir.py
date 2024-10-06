from menu_admin import menuAdmin

def login():
    print("    ==================================================    ")
    print("  ====                                              ====  ")
    print("====                                                  ====")
    print("  ====                                              ====  ")
    print("    ==================================================    ")
    print(" ")
    print("               <<========================>>               ")
    print("            <<<<       Login Sebagai      >>>>            ")
    print("               <<========================>>               ")
    print(" ")
    print("                       1. Admin")
    print("                       2. Kasir")
    print("                       3. Keluar")
    print(" ")
    pilihan = input("Masukan Pilihan : ")
    print("")

    # Login
    while True:
        if pilihan == "1":
            id_admin = input("Masukan Username : ")
            pw_admin = input("Masukan Password : ")
            if id_admin == "admin" and pw_admin == "admin123":
                print("Selamat Anda Berhasil Login!")
                menuAdmin()  # Masuk ke menu admin
                break  # Keluar dari loop setelah login berhasil
            else:
                print("Username dan Password Salah!")
                continue
        elif pilihan == "2":
            id_kasir = input("Masukan Username : ")
            pw_kasir = input("Masukan Password : ")
            if id_kasir == "kasir" and pw_kasir == "kasir123":
                print("Selamat Anda Berhasil Login!")
                # Implementasi untuk menu kasir bisa ditambahkan di sini
                break
            else:
                print("Username dan Password Salah!")
                continue
        elif pilihan == "3":
            print("Terimakasih!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")
            break
