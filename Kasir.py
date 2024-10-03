from menu_admin import menuAdmin
print("    ==================================================    ")
print("  ====                                              ====  ")
print("====                                                  ====")
print("  ====                                              ====  ")
print("    ==================================================    ")
print(" ")
print(" ")
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
while True :
    if pilihan in ["1"] :
            id_admin = input("Masukan Username : ")
            pw_admin = input("Masukan Password : ")
            if id_admin in ["admin"] and pw_admin in ["admin123"]:
                print("Selamat Anda Berhasil Login!")
                menuAdmin()
            else :
                print ("Username dan Password Salah!")
                continue
    if pilihan in ["2"] :
            id_kasir = input("Masukan Username : ")
            pw_kasir = input("Masukan Password : ")
            if id_kasir in ["kasir"] and pw_kasir in ["kasir123"]:
                print("Selamat Anda Berfrey Login!")
                break
            else :
                print ("Username dan Password Salah!")
                continue
    elif pilihan in ["3"]:
            print ("Terimakasih!")
            break
        