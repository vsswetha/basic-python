#1.Print multiplication table of a given number 12

num = 12

# Iterate 10 times from i = 1 to 10
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)



   
#2.Accept number from user and calculate the sum of all number from 1 to a given number 10

n = int(input("Enter number"))
sum = 0
for num in range(1, n + 1):
    sum = sum + num
print("Sum of numbers is: ", sum)


#3..Display numbers from -10 to -1 using for loop
for i in range(-10,-0):
    print (i)
    i-=1




#4.Display a message “Done” after successful execution of for loop

for i in range(5):
    print(i)
else:
    print("Done!")
