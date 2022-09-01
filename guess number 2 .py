#guess number
answer = 22

print("Lets start play the guessing number game" )
while True :
  guess = int(input("What a two-digit number am I thinking of?"))

  if guess < answer :
    print("Little higher...")
  elif guess > answer :
    print("Little lower...")
  else:
    print("Are you MİNDREADER!!")
    break