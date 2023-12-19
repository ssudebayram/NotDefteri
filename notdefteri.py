notlar = {}

while True:
    print("\nNot Defteri Uygulaması")
    print("1. Not Ekle")
    print("2. Notları Listele")
    print("3. Not Sil")
    print("4. Çıkış")

    secim = input("Yapmak istediğiniz işlemi seçin (1-4): ")

    if secim == "1":
        baslik = input("Not başlığını girin: ")
        icerik = input("Not içeriğini girin: ")
        notlar[baslik] = icerik
        print("not eklendi.")
        break
    elif secim == "2":
        if not notlar:
            print("Not defteriniz boş.")
            break
        else:
            print("Notlarınız:")
            for baslik, icerik in notlar.items():
                print(f"- {baslik}: {icerik}")
                break
    elif secim == "3":
        baslik = input("Silmek istediğiniz not başlığını girin: ")
        if baslik in notlar:
            del notlar[baslik]
            print("not silindi.")
        else:
            print("Bu başlıkta bir not bulunamadı.")
            break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
