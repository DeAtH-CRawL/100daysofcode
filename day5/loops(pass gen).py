letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
           'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

import random
#easy mode 1st
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
letterlist=[]
numberlist=[]
symbollist=[]
for i in range (1,nr_letters+1):
    randomLetter=random.choice(letters)
    letterlist.append(randomLetter)

for i in range (1,nr_symbols+1):
    randomSymbol=random.choice(symbols)
    symbollist.append(randomSymbol)

for i in range (1,nr_numbers+1):
    randomNumber=random.choice(numbers)
    numberlist.append(randomNumber)


passwordlist=letterlist+symbollist+numberlist
for password in passwordlist:
    print(password,end='')

#hard mode 2nd
print("\n \n \nyour password in hard mode is: ",end='')
random.shuffle(passwordlist)
for password in passwordlist:
    print(password,end='')