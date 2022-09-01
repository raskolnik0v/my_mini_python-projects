# Input komutunu kullanarak kullanıcıdan int(tam sayı) değer alıyoruz
sayi1=int(input(("Birinci sayıyı giriniz: ")))
sayi2=int(input("İkinci sayıyı giriniz: "))
# Input komutunu kullanarak kullanıcıdan yapacağı işlemin değerini alıyoruz.
islem=int(input("İşlem numarasını giriniz:1-Toplama 2-Çıkarma 3-Çarpma 4-Bölme "))
# Kullanıcının girdiği işlem numarasını kontrol ediyoruz
if (islem==1):
    print("Sonuç: ",int(sayi1+sayi2))
elif (islem==2):
    print("Sonuç: ",int(sayi1-sayi2))
elif (islem==3):
    print("Sonuç: ",int(sayi1*sayi2))
elif(islem==4):
    print("Sonuç: ",float(sayi1/sayi2))
else:
    print("Geçersiz işlem")