#------------------#
# ARMSTRONG NUMBERS #
#------------------#

 # 1 . (371) = (3 ** 3) + (7 ** 3) + (1 ** 3) = 27 + 343 + 1 = 371
 # 2 . (1634) = (1 ** 4) + (6 ** 4) + (3 ** 4) + (4 ** 4) = 1 + 1296 + 81 + 256 = 153

#CODE

while True :
    number = input("Enter a positive integer number :")
    digits = len(number)
    summ = 0
    if not number.isdigit():
        print(number, "is invalid entry.Please enter valid input")
    elif int(number) >= 0 :
        for i in range(digits):
            summ = summ + int(number[i]) ** digits 
        if summ == int(number):
            print(number, "is an Armstrong Number. ")
            break
        else :
            print(number, "is not an Armstrong Number. ")
            break
