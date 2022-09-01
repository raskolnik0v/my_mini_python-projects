from random import choice

words = [
    choice(["Enchanting", "Amazing", "Colourful", "Delightful", "Delicate"]),
    choice(["visions", "distance", "conscience", "process", "chaos"]),
    choice(["superstitious", "contrasting", "graceful", "inviting", "contradicting", "overwhelming"]),
    choice(["true", "dark", "cold", "warm", "great"]),
    choice(["scenery","season", "colours","lights","Spring","Winter","Summer","Autumn"]),
    choice(["undeniable", "beautiful", "irreplaceable", "unbelievable", "irrevocable"]),
    choice(["inspiration", "imagination", "wisdom", "thoughts"])
]

print(("-" * 30) + "\nHaiku Generator\n" + ("-" * 30))
print("{} {},\n{} {} {},\n{} {}.".format(*words))