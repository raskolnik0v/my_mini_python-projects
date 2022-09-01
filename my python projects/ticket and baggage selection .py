bagaj =int(input("Lütfen 1 kg-30 kg arası bagaj seçimi yapınız "))
bilet = int(input("Lütfen 1-30 arası bilet numarası seçiniz "))


if (1<= bagaj <= 15 and 1<= bilet <=10 ):
    print("15 kg'ye kadar olan bagaj ücreti : 20 TL'dir")
    print("1-10 arası bilet ücreti : 100 TL'dir")
    print("Toplam ücret : 120 TL'dir")
elif (1<= bagaj <= 15 and 11<= bilet <= 20): 
    print("15 kg'ye kadar olan bagaj ücreti : 20 TL'dir")
    print("11-20 arası bilet ücreti : 80 TL'dir")
    print("Toplam ücret : 100 TL'dir")
elif (1<= bagaj <= 15 and 21<= bilet <= 30): 
    print("15 kg'ye kadar olan bagaj ücreti : 20 TL'dir")
    print("21-30 arası bilet ücreti : 60 TL'dir")
    print("Toplam ücret : 80 TL'dir")  


elif (16<= bagaj <= 20 and 1<= bilet <= 10): 
    print("15-20 kg'ye kadar olan bagaj ücreti : 30 TL'dir")
    print("1-10 arası bilet ücreti : 100 TL'dir")
    print("Toplam ücret : 130 TL'dir") 
elif (16<= bagaj <= 20 and 11<= bilet <= 20): 
    print("15-20 kg'ye kadar olan bagaj ücreti : 30 TL'dir")
    print("11-20 arası bilet ücreti : 80 TL'dir")
    print("Toplam ücret : 110 TL'dir") 
elif (16<= bagaj <= 20 and 21<= bilet <= 30): 
    print("15-20 kg'ye kadar olan bagaj ücreti : 30 TL'dir")
    print("21-30 arası bilet ücreti : 60 TL'dir")
    print("Toplam ücret : 90 TL'dir") 


elif (21<= bagaj <= 30 and 1 <= bilet<= 10): 
    print("21-30 kg'ye kadar olan bagaj ücreti : 40 TL'dir")
    print("1-10 arası bilet ücreti : 100 TL'dir")
    print("Toplam ücret : 140 TL'dir") 
elif (21<= bagaj <= 30 and 11 <= bilet <= 20): 
    print("21-30 kg'ye kadar olan bagaj ücreti : 40 TL'dir")
    print("11-20 arası bilet ücreti : 80 TL'dir")
    print("Toplam ücret : 120 TL'dir") 
elif (21<= bagaj <= 30 and 21 <= bilet <= 30): 
    print("21-30 kg'ye kadar olan bagaj ücreti : 40 TL'dir")
    print("21-30 arası bilet ücreti : 60 TL'dir")
    print("Toplam ücret : 100 TL'dir") 

else:
    print("Lütfen 1-30 arası değerler giriniz...")

print("Bizi tercih ettiğiniz içn teşekkür ederiz...!")