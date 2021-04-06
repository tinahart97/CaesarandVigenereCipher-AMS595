# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 09:58:56 2020

@author: tinah
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 14:05:29 2020

@author: tinah
"""
from tkinter import *
import random 
import pandas as pd
import string

root = Tk() 
root.geometry("800x500") 
root.title("Christina Hartnett AMS 595 Project") 
  
toplabel = Frame(root, width = 100, relief = SUNKEN) 
toplabel.pack(side = TOP) 
  
root2 = Frame(root, width = 200, height =200, relief = SUNKEN) 
root2.pack(side = LEFT) 
  
  
labellInfo = Label(toplabel, font = ('times', 20, 'bold'), 
                  text = "Caesar Shift Cipher \n AMS 595 Final Project \n The Encryption Key should be an integer\n When the key is a positive integer it shifts the word to the right, \n when negative it shifts the word to the left", 
                   fg = "Navy", bd = 10, anchor='w') 
                       
labellInfo.grid(row = 0, column = 0) 
 
                          
labellInfo.grid(row = 1, column = 0) 
  
rand = StringVar() 
input1 = StringVar() 
key = StringVar()  
Result = StringVar() 

# Users input
Input1 = Label(root2, font = ('times', 20, 'bold'), 
         text = "Input:", bd = 10)
           
Input1.grid(row = 0, column = 1) 
  
Input1 = Entry(root2, font = ('times', 20, 'bold'), 
         textvariable = input1 , bd = 3, insertwidth = 1, 
                bg = "white", justify = 'right' ) 
                  
Input1.grid(row = 0, column = 2) 

# The Key
key1 = Label(root2, font = ('times', 20, 'bold'), 
            text = "Ecryption Key:", bd = 16)
key1.grid(row = 3, column = 1) 
  
key1 = Entry(root2, font = ('times', 20, 'bold'), 
         textvariable = key, bd = 3, insertwidth = 1,
                  bg = "white", width= 4, justify = 'right')
                  
key1.grid(row = 3, column = 2) 


# The results
Result1 = Label(root2, font = ('times', 20, 'bold'), 
             text = "Result:", bd = 16, anchor = "w") 
               
Result1.grid(row = 4, column = 1) 
  
  
Result1 = Entry(root2, font = ('times', 20, 'bold'),  
             textvariable = Result, bd = 0, insertwidth = 0, 
                bg = "grey", justify = 'right' )
                         
Result1.grid(row = 4, column = 2) 

# exit function 
def qExit(): 
    root.destroy() 
  
# reset it
def Reset(): 
    rand.set("") 
    input1.set("") 
    key.set("") 
    Result.set("") 
  

#Function to encode 
def encode2(key, clear): 
    dictionaryinitial = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 
                         'h': 8,'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 
                         'n': 14,'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 
                         't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24,  'y': 25, 
                         'z': 26}
    eninputlower= clear.lower(); #make words lowercase
    key= int(key)
    splitword= list(eninputlower);
    newlabel= [dictionaryinitial[k] for k in splitword if k in dictionaryinitial] # match letters to their key
    # adjusting the dictionary for the new key
    for k, v in dictionaryinitial.items():
        dictionaryinitial[k] = (v - key)
    newdictionary= dictionaryinitial
    # making sure the numbers are between 1 and 26
    for l, w in newdictionary.items(): 
        if w > 26:
            newdictionary[l] = (w - 26)
        elif w < 1:
            newdictionary[l] = (w + 26)
    newdict= newdictionary
    #newlabel= [x - 1 for x in newlabel]
    dictionaryinitial1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 
                         'h': 8,'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 
                         'n': 14,'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 
                         't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24,  'y': 25, 
                         'z': 26}
    
    new_dict = {}
    for k, v in newdict.items():
        new_dict[v] = k
        
    newlabel1= [new_dict[k] for k in newlabel if k in new_dict]
    return(''.join(newlabel1))
    
  
def Ans(): 
    clear = input1.get() 
    k = key.get() 
    Result.set(encode2(k, clear)) 

  
#Result button
Result2 = Button(root2, padx = 10, pady = 5, bd = 10, fg = "White", 
                        font = ('times', 15, 'bold'), width = 10, 
                       text = "Result", bg = "SkyBlue3", 
                         command = Ans).grid(row = 7, column = 1) 
  
#Reset button 
Reset1 =  Button(root2, padx = 10, pady = 5, bd = 10, fg = "White", 
                        font = ('times', 15, 'bold'),
                    width = 10, text = "Reset", bg = "SkyBlue3", 
                   command = Reset).grid(row = 7, column = 2) 
  
#Exit button 
Exit1 =  Button(root2, padx = 10, pady = 5, bd = 10, fg = "White", 
                        font = ('times', 15, 'bold'),
                      width = 10, text = "Exit", bg = "SkyBlue3", 
                  command = qExit).grid(row = 7, column = 3) 
  
root.mainloop()


