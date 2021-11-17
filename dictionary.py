#1.Convert two list into dictionary
a = ["Ram", "jerry", "tom"]
b = [1, 4, 5]
  
# Printing original keys-value lists
print ("Original key list is : " + str(a))
print ("Original value list is : " + str(b))
  
# using naive method
# to convert lists to dictionary
res = {}
for key in a:
    for value in b:
        res[key] = value
        b.remove(value)
        break  
  
# Printing resultant dictionary 
print ("Resultant dictionary is : " +  str(res))


#2.combine two Python dictionaries into one
def Merge(dict1, dict2):
    return(dict2.update(dict1))
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
 
# This return None
print(Merge(dict1, dict2))
 
# changes made in dict2
print(dict2)

#3.rename the key in dictionary


dict = {'jerry': 1, 'jack' : 5,
            'tom' : 10, 'jin' : 15}
  
# printing initial json
print ("initial 1st dictionary", dict)
  
# changing keys of dictionary
dict['jimin'] = dict['jin']
del dict['jin']
  
  
# printing final result
print ("final dictionary", str(dict))
