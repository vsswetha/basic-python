#Set Exercises:
#1.Write a Python program to remove all elements from a given set


a = {"hi", "hello", "good"}
print("Original set elements:")
print(a)        
print("\nAfter removing all elements of the said set.")
a.clear()
print(a)






#2. Write a program to remove the duplicates from the list

a = [10,20,30,20,10,50,60,40,80,50,40]

dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print(dup_items)





#3.Write a Python program to remove all elements from a given set

a = {"hi", "hello", "good"}
print("Original set elements:")
print(a)        
print("\nAfter removing all elements of the said set.")
a.clear()
print(a)




#4.find the elements in a given set that are not in another set.
sn1 = {1,2,3,4,5}
sn2 = {4,5,6,7,8}
print("Original sets:")
print(sn1)
print(sn2)
print("Difference of sn1 and sn2 using difference():")
print(sn1.difference(sn2))
print("Difference of sn2 and sn1 using difference():")
print(sn2.difference(sn1))





#5. program to remove the intersection of a 2nd set from the 1st set

sn1 = {1,2,3,4,5}
sn2 = {4,5,6,7,8}
print("Original sets:")
print(sn1)
print(sn2)
print("\nRemove the intersection of a 2nd set from the 1st set using difference_update():")
sn1.difference_update(sn2)
print("sn1: ",sn1)
print("sn2: ",sn2)





