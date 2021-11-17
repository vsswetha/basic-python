# 1. randomize the items of a list in place in Python
import random

mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)

print(mylist)

 #2. Python program to interchange first and last elements in a list
# Swap function
def swapList(newList):
    size = len(newList)
     
    # Swapping
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp
     
    return newList
     
# Driver code
newList = [12, 35, 9, 56, 24]
 
print(swapList(newList))


 #3. Python program to interchange first and last elements in a list

# Swap function
def swapList(newList):
    size = len(newList)
     
    # Swapping
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp
     
    return newList
     
# Driver code
newList = [10, 20, 30, 40, 50]
 
print(swapList(newList))

# 4. python program for converting weight from kgs to pounds and vice versa

kilo_grams = float(input('Enter weight in Kg to Convert into pounds:'))
pounds = kilo_grams * 2.2046
print(kilo_grams,' Kilograms =', pounds,' Pounds')



pounds = float(input('Enter weight in Pounds(Lbs) to Convert into Kilograms:'))
kilo_grams = pounds * 0.453592
print(pounds,' Pounds (Lbs) are equal to', kilo_grams,'Kilograms (Kgs)')
