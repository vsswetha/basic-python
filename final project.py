#find the longest words.

def longest_word(filename):
    with open(filename, 'r') as infile:
              words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

print(longest_word('long.txt'))




#Print the number of distinct words and number of occurrences in txt file


def count_words(filepath):
   with open(filepath) as f:
       data = f.read()
       data.replace(",", " ")
       return len(data.split(" "))
print(count_words("testfile.txt"))




#--------------------------------------
import random
l1= [2,3,4,5]
l2=["days ago","weeks ago","months ago","years ago"]
l3=["man","woman","child","person"]
l4=["went","go","come","reach"]
l5=["park","hotel","abroad","shopping"]
print(random.choice(l1),random.choice(l2),random.choice(l3),random.choice(l4),random.choice(l5))
#------------------------------------

import pyqrcode
from pyqrcode import QRCode

url = "https://www.youtube.com/watch?v=mPVDGOVjRQ0"
qr = pyqrcode.create(url)
qr.svg("subscribe.svg",scale=5)

#----------------------------------------

from tkinter import *
window = Tk()

window.geometry("400x250")  
  
#creating label  
uname = Label(window, text = "Username").place(x = 30,y = 50)  
  
#creating label  
password = Label(window, text = "Password").place(x = 30, y = 90)  
  
  
sbmitbtn = Button(window, text = "Submit",activebackground = "pink", activeforeground = "blue").place(x = 30, y = 120)  
  
e1 = Entry(window,width = 20).place(x = 100, y = 50)  
  
  
e2 = Entry(window, width = 20).place(x = 100, y = 90) 

window.mainloop()

#----------------------------------------

from tkinter import *
 
 
# Create a GUI window
window = Tk()
  
# Function to convert weight
# given in kg to grams, pounds
# and ounces
def from_kg():
     
    # convert kg to gram
    gram = float(e2_value.get())*1000
     
    # convert kg to pound
    pound = float(e2_value.get())*2.20462
     
    # convert kg to ounce
    ounce = float(e2_value.get())*35.274
     
    # Enters the converted weight to
    # the text widget
    t1.delete("1.0", END)
    t1.insert(END,gram)
     
    t2.delete("1.0", END)
    t2.insert(END,pound)
     
    t3.delete("1.0", END)
    t3.insert(END,ounce)
 
# Create the Label widgets
e1 = Label(window, text = "Enter the weight in Kg")
e2_value = StringVar()
e2 = Entry(window, textvariable = e2_value)
e3 = Label(window, text = 'Gram')
e4 = Label(window, text = 'Pounds')
e5 = Label(window, text = 'Ounce')
 
# Create the Text Widgets
t1 = Text(window, height = 1, width = 20)
t2 = Text(window, height = 1, width = 20)
t3 = Text(window, height = 1, width = 20)
 
# Create the Button Widget
b1 = Button(window, text = "Convert", command = from_kg)
 
# grid method is used for placing
# the widgets at respective positions
# in table like structure
e1.grid(row = 0, column = 0)
e2.grid(row = 0, column = 1)
e3.grid(row = 1, column = 0)
e4.grid(row = 1, column = 1)
e5.grid(row = 1, column = 2)
t1.grid(row = 2, column = 0)
t2.grid(row = 2, column = 1)
t3.grid(row = 2, column = 2)
b1.grid(row = 0, column = 2)
 
# Start the GUI
window.mainloop()

#-------------------------------------------

#User defined modules:
#mod1.py:
#---------
'''person = {
  "name": "Raju",
  "age": 20,
  "country": "India"
}
x=[3,90,56]

def greet(msg):
  print("Hello, " + msg)

def add(a,b):
    print(a+b)'''
    


#callmod.py:
#-------------

import mod1

mod1.greet("python")
mod1.add(13,34)
a = mod1.person["name"]
print(a)
y= mod1.x
print(y)



