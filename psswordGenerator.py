letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
          'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+']

print("welcome to the password generator ")

nr_letters = int(input("How many letters would you like in your password? "))
nr_symbols = int(input("How many symbols would you like? "))        
nr_numbers = int(input("How many numbers would you like? "))
import random 
pasword_list = []
import random 
for _ in range(0, nr_letters):
    pasword_list.append(random.choice(letters) )

for _ in range (0, nr_numbers):
    pasword_list.append( random.choice(numbers) )


for _ in range (0, nr_symbols):
    pasword_list.append(random.choice(symbols) )

random.shuffle(pasword_list)



password = "".join(pasword_list)
print(password)

    

