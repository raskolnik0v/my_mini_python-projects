vize = int(input("Lütfen vize notunuzu giriniz:"))
final = int(input("Lütfen final notunuzu giriniz:"))
sonuc = float(vize * 40/100) + (final * 60/100)
print(sonuc)
if (final < 45):
      print("Final notunuz 45'den küçük olduğu için dersten kaldınız")
if (sonuc >= 45):
      print("Dersi başarıyla geçtiniz.Tebrikler.")
else:
      print("Başarısız")
      