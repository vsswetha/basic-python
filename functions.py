
#1.check whether a number is in a given range using functions
def testrange(n):
    if n in range(3,9):
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
testrange(5)


#2.Create a user defined function for finding the area of circle


def findArea(r): 
    PI = 3.142
    return PI * (r*r); 
  
# Driver method
num=float(input("Enter r value:"))
print("Area is %.6f" % findArea(num)); 
  

#3. Pass a list as argument and sum all the values in the list




total = 0
 
# creating a list
list1 = [11, 5, 17, 18, 23]
 
# Iterate each element in list
# and add them in variable total
for ele in range(0, len(list1)):
    total = total + list1[ele]
 
# printing total value
print("Sum of all elements in given list: ", total)


#4.Write a Python function to convert temperatures to and from Celsius, Fahrenheit. [ Formula: c = (f-32)(5/9)
celsius = float(input("Enter temperature in celsius: "))
fahrenheit = (celsius * 9/5) + 32
print('%.2f Celsius is: %0.2f Fahrenheit' %(celsius, fahrenheit))
