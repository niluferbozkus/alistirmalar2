import random

tahmin=input("Mastermind;\n*10 ile 98 arasında (10 ve 98 dahil),\n*Basamakları farklı\nbir sayı tutmuştur.\nMastermind'ın tuttuğu sayı için tahmininzi giriniz: ")

sayi=random.randint(10,98)

while True :
    if int(tahmin)>=10 and int(tahmin)<=98:
        tahmin = tahmin
        dogruyer=0
        yanlisyer=0
        if tahmin[0]== tahmin[1]:
            print("Lütfen rakamları birbirinden farklı sayılar girin!")
            tahmin=input("Mastermind'ın tuttuğu sayı için tahmininzi giriniz: ")
        else :
            if tahmin[0] ==(str(sayi))[0] and tahmin[1]==(str(sayi))[1]:
                dogruyer += 2
                print("Tebrikler, sayıyı doğru tahmin ettiniz!!!")
                break
            elif tahmin[0] ==(str(sayi))[0] or tahmin[1]==(str(sayi))[1]:
                dogruyer += 1
            elif tahmin[0]==(str(sayi))[1] and tahmin[1]==(str(sayi))[0]:
                yanlisyer -= 2
            elif tahmin[0]==(str(sayi))[1] or tahmin[1]==(str(sayi))[0]:
                yanlisyer -= 1
       
        print("Sizin tahmininiz: ",tahmin)
        print("Doğru yer: " , dogruyer)
        print("Yanlış yer: " , yanlisyer)
        tahmin=input("Mastermind'ın tuttuğu sayı için tahmininzi giriniz: ")
        
    else  :
        print("Lütfen doğru aralıkta sayılar girin! ")
        tahmin=input("Mastermind'ın tuttuğu sayı için tahmininzi giriniz: ")


