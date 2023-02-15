#Remember import random function here:
import random

my_list = [4,5,734,43,45]

#The magic is here:

for x in range(10):
    random_number=random.randint(0, 10)
    my_list.append(random_number)

print(my_list)