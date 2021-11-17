
'''Conditional statements:
1.Write an if statement that asks for the user's name via input() function.
print "Good Morning" + the name got as input

2.Write a program to accept percentage from the user and display the grade according to the following criteria:

         Marks                                    Grade
         > 95                                         A
         > 80 and <= 95                               B
         >= 50 and <= 80                              C
         below 50                                     D

3. Write a program to check whether a number is divisible by 6 or not.

4.check whether a number entered by user is even or odd.

5.Get the age input from user and check whether a person is eligible for voting or not.'''





#1
a=input("enter the user name")
b="good morning"
c=b+a
print(c)


#2
a=int(input("enter the marks"))

if a>95:
    print( "GRADE A")

elif a>80 and a<=95:
    print("GRADE B")

elif a>=50 and a<=80:
    print("GRADE C")

else:  
    print("GRADE D")

#3


a=int(input("enter the no"))
if(a%6==0):
    print("the given no divide by 6")
else:
    print("the given no not divide by 6")

#4

a=int(input("enter the no"))
if(a%2==0):
    print("the given no is even")
else:
    print("the given no is odd")


#5

 
age=int(input("enter the age"))
if age>=18 and age<60:
    print("eligible to  drive")
else:
     print("not eligible to drive")
