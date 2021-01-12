###Let's make an algorithm to sort a list 
import random

#First, let's generate our list composed from random numbers
my_list = []
for i in range(100):
    my_list.append(random.randint(1,100))



sorted_list = []
while my_list != []:
    minimum = min(my_list)
    sorted_list.append(minimum)
    my_list.pop(my_list.index(minimum))

print(sorted_list)