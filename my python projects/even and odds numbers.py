#even and odds numbers


evens = []
odds = [] 

for i in range(10) :
  if i % 2 == 0 :
    evens.append(i)
  else:
    odds.append(i)
print("evens :", evens)
print("odds :" , odds)

**************************
number = [11, 2, 24, 61, 48, 33, 3]

evens = []
odds = [] 

for i in number :
  if i % 2 == 0 :
    evens.append(i)
    
  else:
    odds.append(i)
    
print("The number of even numbers :", len(evens))
print("The number of odd numbers :", len(odds))

******************************
numbers = (11,22,45,36,3,24,99,78,45,4,2,66,5)
evens = 0
odds = 0

for i in numbers:             #bu sayaç yöntemi saydırmayla oluyor her seferinde 1 artsın diye += 1 yapıyoruz
                              #yukarıdaki aynı sorunun len ile çözümü
  
  if i % 2 == 0:
    evens += 1
   
  else:
    odds += 1
   
print("The number of odds numbers :",odds)
print("The number of even numbers :", evens)