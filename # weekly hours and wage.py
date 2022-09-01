# weekly hours and wage

hours =int(input("Plase enter your weekly working hours "))
if hours <= 40:
   wage = hours * 20
else:
   wage = (hours - 40) * 20 * 1.5 + 40 * 20 
print("Your weekly wage is $" , wage) 