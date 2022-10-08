PASSWORD GENERATOR.py

import random

uppers =[chr(random.randint(65,90)) for i in range(3)]  #rastgele 3 büyük harf ürettik

lowers =[chr(random.randint(97,120)) for i in range(3)] 

numbers = [chr(random.randint(48,57)) for i in range(3)] 

chars = chr(random.randint(33,47)) + chr(random.randint(58,64)) 

uppers =[chr(random.randint(65,90)) for i in range(3)]
lowers =[chr(random.randint(97,120)) for i in range(3)] 
numbers = [chr(random.randint(48,57)) for i in range(3)]
chars = chr(random.randint(33,47)) + chr(random.randint(58,64)) 


password = ("".join(uppers) + "".join(lowers) + "".join(numbers) + "".join(chars))

password


############################## ** OR ** ############################

#PASSWORD GENERATOR
#10 DIGIT, MIXED PASSWORD

import random

uppers =[chr(random.randint(65,90)) for i in range(3)]  #rastgele 3 büyük harf ürettik

lowers =[chr(random.randint(97,120)) for i in range(3)] 

numbers = [chr(random.randint(48,57)) for i in range(3)] 

chars = chr(random.randint(33,47)) + chr(random.randint(58,64)) 

uppers =[chr(random.randint(65,90)) for i in range(3)]
lowers =[chr(random.randint(97,120)) for i in range(3)] 
numbers = [chr(random.randint(48,57)) for i in range(3)]
chars = chr(random.randint(33,47)) + chr(random.randint(58,64)) 

def mixer (password):
  templist =  list(password)
  random.shuffle(templist)
  return "".join(templist)

print(mixer(password))
