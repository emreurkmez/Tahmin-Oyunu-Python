def tahmin_oyunu():
    tahmin_hakki = 8
    alt_sinir = 1
    ust_sinir = 100

    print("1 ile 100 arasında bir sayı tutun.")

    for deneme in range(tahmin_hakki):
        tahmin = (alt_sinir + ust_sinir) // 2 

        print("Tahminim:", tahmin)

        cevap = input("Doğru mu? (Evet/Hayır): ")

        if cevap.lower() == "evet":
            print("Yapay zeka dünyayı fethediyor! Tahminim doğru.")
            return
        elif cevap.lower() == "hayır":
            yukari_mi = input("Daha yukarı mı? (Evet/Hayır): ")
            if yukari_mi.lower() == "evet":
                alt_sinir = tahmin + 1
            else:
                ust_sinir = tahmin - 1
        else:
            print("Geçersiz bir cevap girdiniz.")

    print("Yapay zeka kaybetti! Tahmin hakkı bitti.")

tahmin_oyunu()
