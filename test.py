def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    if y == 0:
        return print("Tidak Dapat Dibagi 0")
    else:
        return x / y 
        
def Kalkulator():
    while True:
        
        print("Pilihan Menu Kalkulator")
        print("1. Tambah")
        print("2. Kurang")
        print("3. Kali")
        print("4. Bagi")
        pilihan = input("pilihlah menu kalkulator di atas 1/2/3/4 atau ketik bye untuk menyudahi:")

        if pilihan in ['bye']:
            print ("see you later!")
            break
        
        if pilihan in ['1', '2', '3', '4',]:
            num1 = float(input("Masukan Angka Pertama :"))
            num2 = float(input("Masukan Angka Kedua :"))

            if pilihan == '1':
                print(f"hasil : {num1} + {num2} = {tambah(num1, num2)}" )
            if pilihan == '2':
                print(f"hasil : {num1} - {num2} = {kurang(num1, num2)}")
            if pilihan == '3':
                print(f"hasil : {num1} * {num2} = {kali(num1, num2)}")
            if pilihan == '4':
                print(f"Hasil : {num1} * {num2} = {bagi(num1, num2)}")
        else:
            print("pilihan tidak valid!")
            


Kalkulator()