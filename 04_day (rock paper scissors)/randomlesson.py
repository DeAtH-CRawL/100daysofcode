import random 
import my_module
random_integer = random.randint(1,10) # generates a random integer between 1 and 10 inclusive
print(random_integer)
print(my_module.my_favourite_number) # prints the favourite number from my_module
random_number = random.random() * 10 # generates a random float between 0 and 10 multiplying the 0-1 range by 10 
print(random_number)
random_float = random.uniform(1,10) # generates a random float between 1 and 10 inclusive 
print(random_float)
