import random

def tahmin_oyunu():
    tahmin_hakki = 6
    dogru_sayi = random.randint(1, 100)  
    
    print("1 ile 100 arasında bir sayıyı tahmin edin.")

    for deneme in range(tahmin_hakki):
        tahmin = int(input("Tahmininiz: "))

        if tahmin < dogru_sayi:
            print("Daha yüksek bir sayı deneyin.")
        elif tahmin > dogru_sayi:
            print("Daha düşük bir sayı deneyin.")
        else:
            print("Tebrikler! Doğru sayıyı buldunuz.")
            return

    print("Maalesef, hakkınız bitti. Doğru sayı:", dogru_sayi)

tahmin_oyunu()
