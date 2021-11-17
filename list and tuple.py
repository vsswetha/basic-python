#List:
#1. Reverse a given list in Python aLsit = [100, 200, 300, 400, 500]


list= [100, 200, 300, 400, 500]
print(list[::-1])


#2.Turn every item of a list into its square a=[1, 2, 3, 4, 5, 6, 7]

numbers = [1, 2, 3, 4, 5, 6, 7]

squarednumbers = [number ** 2 for number in numbers]

print(squarednumbers)



#3.Print the third item in the  list. a=[11,34,67,78,77,89]

a = [11,34,67,78,77,89]
thirditem= a[2]


print(thirditem)

#4. find the length of the list a=[11,34,67,78,77,89]

a= [ 11,34,67,78,77,89]
print(len(a))





#5. Change the value from 67 to 76 in the list a=[11,34,67,78,77,89]

a = [11,34,67,78,77,89]
a[2] = 76
print(a)










#1) create a tuple with one item and print it.



thistuple = ("good",)
print(thistuple)



#2)Write a Python program to convert a tuple to a string.



tup = ('h', 'a', 'p', 'p', 'y')
str =  ''.join(tup)
print(str)
#3)Write a Python program to remove an item from a tuple.


tuplex = "g", "o", "o", "o", "d"

print(tuplex)
tuplex = tuplex[:2] + tuplex[3:]
print(tuplex)

