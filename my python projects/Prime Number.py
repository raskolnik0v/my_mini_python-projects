## Prime Number ##,

#Prime Number = 2, 3, 5, 7, 11, 13, 17,19,23,29,31 .......

#CODE


n = int(input("Enter a positivenumber int number to check if it is a Prime Number "))
counter = 0

for i in range (1,n+1):
    if n % i == 0 :
        counter += 1
if (n == 0) or (n ==1) or (counter >= 3):
    print(n, "is not a Prime Number ")
else:
    print(n, "is a Prime Number ")