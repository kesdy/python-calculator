import math

while True:
    print("""
     Toplama işlemleri için : 1
     Çıkarma işlemleri için : 2
     Çarpma işlemleri için : 3
     Bölme işlemleri için : 4
     Faktöriyel işlemleri için : 5
          ÇIKIŞ : 0
     """)

    try:
        secim = int(input("Bir sayı seçiniz : "))

        if secim == 1:
            try:
                mesaj1 = int(input("Bir sayı giriniz : "))
                mesaj2 = int(input("2. sayıyı giriniz : "))
                islem = mesaj1 + mesaj2
                print("Sonuç : ", islem)
            except ValueError:
                print("HATA | Lütfen geçerli bir sayı giriniz.")

        elif secim == 2:
            try:
                mesaj3 = int(input("Bir sayı giriniz : "))
                mesaj4 = int(input("2. sayıyı giriniz : "))
                islem2 = mesaj3 - mesaj4
                print("Sonuç : ", islem2)
            except ValueError:
                print("HATA | Lütfen geçerli bir sayı giriniz.")

        elif secim == 3:
            try:
                mesaj5 = int(input("Bir sayı giriniz : "))
                mesaj6 = int(input("2. sayıyı giriniz : "))
                islem3 = mesaj5 * mesaj6
                print("Sonuç : ", islem3)
            except ValueError:
                print("HATA | Lütfen geçerli bir sayı giriniz.")

        elif secim == 4:
            try:
                mesaj7 = int(input("Bir sayı giriniz : "))
                mesaj8 = int(input("2. sayıyı giriniz : "))

                if mesaj8 == 0:
                    print("HATA | 0'a bölünme işlemleri yapılamaz.")
                else:
                    islem4 = mesaj7 / mesaj8
                    print("Sonuç : ", islem4)
            except ValueError:
                print("HATA | Lütfen geçerli bir sayı giriniz.")

        elif secim == 5:
            try:
                mesaj9 = int(input("Bir sayı giriniz : "))

                if mesaj9 < 0:
                    print("HATA | Faktöriyel negatiflik içeremez.")
                else:
                    islem5 = math.factorial(mesaj9)
                    print("Sonuç : ", islem5)
            except ValueError:
                print("HATA | Lütfen geçerli bir sayı giriniz.")

        elif secim == 0:
            print("Programdan çıkılıyor...")
            break

        else:
            print("HATA | Geçersiz bir seçim yaptınız. Lütfen geçerli bir seçenek giriniz.")

    except ValueError:
        print("HATA | Lütfen geçerli bir sayı seçiniz.")
