import random


list1 = input("Enter your input:").split(',')

random.shuffle(list1)
print(list1)
random.shuffle(list1)

#print(list1)
str1= ' '.join(list1)
print(str1)
