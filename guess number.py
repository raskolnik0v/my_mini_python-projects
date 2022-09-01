Bilgisayarın 1-100 arasında seçtiği sayıyı tahmin haklarımız bitene kadar tahmin etmeye çalıştık.

random.randint fonksiyonu ile parantez içinde belirtilen aralıkta bir sayıyı rastgele seçiyoruz.
time.sleep fonksiyonu ile parantez içindeki değer kadar saniye programı duraklatıyoruz.

import random
import time
print("Sayı tahmin oyununa hoş geldiniz!n 1-100 arasında bir sayı tahmin edin")
sayi = random.randint(1,100)
tahmin_hakki = 5
while True:
    tahmin = int(input("Tahmininiz: "))
    
    if tahmin == sayi:
        print("Sayı sorgulanıyor... ")
        time.sleep(1)
        print("Tebrikler! doğru bildiniz")
        break
    elif tahmin > sayi:
        print("Sayı sorgulanıyor... ")
        time.sleep(1)
        tahmin_hakki-=1
        print("Daha küçük küçük bir sayı giriniz")
        print("Kalan tahmin hakkı: ",tahmin_hakki)
    else:
        print("Sayı sorgulanıyor... ")
        time.sleep(1)
        tahmin_hakki -= 1
        print("Daha büyük bir sayı giriniz")
        print("Kalan tahmin hakkı: ", tahmin_hakki)
    if tahmin_hakki == 0:
        print("Tahmin hakkınız bitmiştir")
        print("Bilgisayarın tahmini: ",sayi)
        break