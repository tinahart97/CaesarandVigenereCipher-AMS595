# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 10:18:54 2020

@author: tinah
"""
from tkinter import *
import random 
import pandas as pd
import string

root = Tk() 
  
root.geometry("1000x400") 
root.title("Christina Hartnett AMS 595 Project") 
  
Tops = Frame(root, width = 100, relief = SUNKEN) 
Tops.pack(side = TOP) 

root2 = Frame(root, width = 100, height = 100, relief = SUNKEN) 
root2.pack(side = LEFT) 
  
lblInfo = Label(Tops, font = ('times', 20, 'bold'), 
          text = "Vigenère cipher \n Both the Message and Keyword should be words \n They do not have to be of equal length", fg = "Black", bd = 10, anchor='w') 
                       
lblInfo.grid(row = 1, column = 0) 

rand = StringVar() 
mess = StringVar() 
key = StringVar() 
mode = StringVar() 
Result = StringVar() 

mess1 = Label(root2, font = ('times', 20, 'bold'), 
         text = "Message:", bd = 16, anchor = "w") 
           
mess1.grid(row = 0, column = 0) 
  
mess1 = Entry(root2, font = ('times', 18, 'bold'), 
         textvariable = mess, bd = 3, insertwidth = 1, 
                bg = "white", justify = 'right' ) 
                  
mess1.grid(row = 0, column = 1) 
  
Key1 = Label(root2, font = ('times', 20, 'bold'), 
            text = "Keyword:", bd = 16, anchor = "w") 
              
Key1.grid(row = 0, column = 2) 
  
Key1 = Entry(root2, font = ('times', 18, 'bold'), 
         textvariable = key,bd = 3, insertwidth = 1, 
                bg = "white", justify = 'right' ) 
                  
Key1.grid(row = 0, column = 3) 
  
Result1 = Label(root2, font = ('times', 20, 'bold'), 
             text = "Result:", bd = 16, anchor = "w") 
               
Result1.grid(row = 1, column = 2) 
  
Result1 = Entry(root2, font = ('times', 20, 'bold'),  
             textvariable = Result, bd = 0, insertwidth = 0, 
                bg = "grey", justify = 'right' )
                         
Result1.grid(row = 2, column = 2) 
  

# Function to encode 
def encode(key, clear): 
    key= key.lower();
    clear= clear.lower();
    lengword= len(clear)
    lengkey= len(key)
    
#adjusting the keyword length to match the plaintext input
    if lengword > lengkey:
        keyword= (key * (lengword//lengkey + 1))[:lengword]
    elif lengword < lengkey:
        keyword= key[:lengword]
    else:
        keyword = key
#creating the dataframe of the alphabet
    alphabet = list(string.ascii_lowercase)
    matrix = []
    for i in range(26):
        matrix.append(list(string.ascii_lowercase[i:]+string.ascii_lowercase[:i]))
    df = pd.DataFrame(matrix,columns = alphabet,index = alphabet)
    
    keyword= keyword.split()
    word= clear.split()

# making the keyword and word inputs to the column labels and row labels
# separating them into each individual letter of the word one by one
# now we will find the corresponding letter of the row and column label given
    keywordlist = [i for ele in keyword for i in ele] 

    wordlist= [j for elem in word for j in elem] 
    holder= []
    for column, row in zip(keywordlist, wordlist):
        x= df.loc[row,column]
        holder.append(x)
    
    return(''.join(holder))

def encode1(): 
    
    clear = mess.get() 
    k = key.get() 
    m = mode.get() 
    m= m.lower()
    Result.set(encode(k, clear)) 

    
# exit function 
def Exitit(): 
    root.destroy() 
  
# Function to reset the window 
def Reset(): 
    rand.set("") 
    mess.set("") 
    key.set("") 
    mode.set("") 
    Result.set("") 
   
    
# Result button
Total1 = Button(root2, padx = 10, pady = 5, bd = 10, fg = "White", 
                        font = ('times', 15, 'bold'), width = 10, 
                       text = "Result", bg = "SkyBlue3", 
                         command = encode1).grid(row = 8, column = 1) 
  
# Reset button 
Reset1 =  Button(root2, padx = 10, pady = 5, bd = 10, fg = "White", 
                        font = ('times', 15, 'bold'),
                    width = 10, text = "Reset", bg = "SkyBlue3", 
                   command = Reset).grid(row = 8, column = 2) 
  
# Exit button 
Exit1 =  Button(root2, padx = 10, pady = 5, bd = 10, fg = "White", 
                        font = ('times', 15, 'bold'),
                      width = 10, text = "Exit", bg = "SkyBlue3", 
                  command = Exitit).grid(row = 8, column = 3) 
  
root.mainloop() 