# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 14:00:47 2020

@author: tinah
"""

from tkinter import *
import random 
import pandas as pd
import string


  
root = Tk()  
root.geometry("870x500") 
root.title("Christina Hartnett AMS 595 Project") 
  
toplabel = Frame(root, width = 100, relief = SUNKEN) 
toplabel.pack(side = TOP) 
  
root2 = Frame(root, width = 200, height =200, relief = SUNKEN) 
root2.pack(side = LEFT) 
  
  
labellInfo = Label(toplabel, font = ('times', 20, 'bold'), 
                  text = "Caesar Shift Cipher \n AMS 595 Final Project \n The Decode hint should be written as two characters equal each other: \n for example, a 6 letter right shift would be A = G"
                   ,fg = "Navy", bd = 10, anchor='w') 
                       
labellInfo.grid(row = 0, column = 0) 
 
                          
labellInfo.grid(row = 1, column = 0) 
  
rand = StringVar() 
input1 = StringVar() 
key1 = StringVar() 
key2 = StringVar() 
mode = StringVar() 
Result = StringVar() 
  

  
# User input
Input1 = Label(root2, font = ('times', 20, 'bold'), 
         text = "Input:", bd = 10)
           
Input1.grid(row = 0, column = 1) 
  
Input1 = Entry(root2, font = ('times', 20, 'bold'), 
         textvariable = input1 , bd = 3, insertwidth = 1, 
                bg = "white", justify = 'right' ) 
                  
Input1.grid(row = 0, column = 2) 
  


# Users Keys
keys1 = Label(root2, font = ('times', 20, 'bold'), 
            text = "Decode hint:", bd = 16, anchor = "w") 
              
keys1.grid(row = 1, column = 1) 
  
keys1 = Entry(root2, font = ('times', 20, 'bold'), 
         textvariable = key1, bd = 3, insertwidth = 1,
                  bg = "white", width= 4, justify = 'right')
                  
keys1.grid(row = 1, column = 2) 


keys2 = Label(root2, font = ('times', 20, 'bold'), 
            text = "=        ", bd = 16, anchor = "w") 
              
keys2.grid(row = 1, column = 3) 

keys2 = Entry(root2, font = ('times', 20, 'bold'), 
         textvariable = key2, bd = 3, insertwidth = 1,
                  bg = "white", width= 4, justify = 'right')
                  
keys2.grid(row = 1, column = 4) 

# Where the result will print
Result1 = Label(root2, font = ('times', 20, 'bold'), 
             text = "Result:", bd = 16, anchor = "w") 
               
Result1.grid(row = 5, column = 1) 
  
Result1 = Entry(root2, font = ('times', 20, 'bold'),  
             textvariable = Result, bd = 0, insertwidth = 0, 
                bg = "grey", justify = 'right' )
                         
Result1.grid(row = 5, column = 2) 

# exit function 
def qExit(): 
    root.destroy() 
  
# reset it
def Reset(): 
    rand.set("") 
    input1.set("") 
    key1.set("") 
    key2.set("") 
    mode.set("") 
    Result.set("") 
  

#Function to decode 
def decode(key1,key2, clear): 
    decinputlower= clear.lower();
    key1= key1.lower();
    key2= key2.lower();
    splitupword= list(decinputlower);
    
        
    dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 
                         'h': 8,'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 
                         'n': 14,'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 
                         't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24,  'y': 25, 
                         'z': 26}
    
    difference = []
#giving each letter a number value
    newlabelkey1=[dictionary[k] for k in key1 if k in dictionary]
    newlabelkey2=[dictionary[k] for k in key2 if k in dictionary]

#how to get the difference in the keys
    zip_object = zip(newlabelkey1, newlabelkey2)
    for list1_i, list2_i in zip_object:
        difference.append(list2_i-list1_i)
    
#change the difference in the keys to a integer so I can apply it 
    strings = [str(diff) for diff in difference]
    print(strings)
    singlestr = "".join(strings)
    integer= int(singlestr)
    
    for k, v in dictionary.items():
        dictionary[k] = (v - integer)
    newdictionary1= dictionary
    
    for l, w in newdictionary1.items():
        if w > 26:
            newdictionary1[l] = (w - 26)
        elif w < 1:
            newdictionary1[l] = (w + 26)
    newdict1= newdictionary1
    
    dictionary1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 
                         'h': 8,'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 
                         'n': 14,'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 
                         't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24,  'y': 25, 
                         'z': 26}
    
    
    newlabel1= [newdict1[k] for k in splitupword if k in newdict1]
    
    
    key_list1 = list(dictionary.keys())
    val_list1 = list(dictionary.values())
    
    newlabel1= [newdict1[k] for k in splitupword if k in newdict1]

    new_dict1 = {}
    for k, v in dictionary1.items():
        new_dict1[v] = k
        
    newlabel12= [new_dict1[k] for k in newlabel1 if k in new_dict1]
    return(''.join(newlabel12))
  
def Ref(): 
    
    clear = input1.get() 
    k1= key1.get()
    k2= key2.get()
    Result.set(decode(k1, k2, clear)) 
  
    
  
# Result Button
Total1 = Button(root2, padx = 10, pady = 5, bd = 10, fg = "black", 
                        font = ('times', 15, 'bold'), width = 10, 
                       text = "Result", bg = "SkyBlue3", 
                         command = Ref).grid(row = 7, column = 1) 
  
# Reset Button 
Reset1 =  Button(root2, padx = 10, pady = 5, bd = 10, fg = "black", 
                        font = ('times', 15, 'bold'),
                    width = 10, text = "Reset", bg = "SkyBlue3", 
                   command = Reset).grid(row = 7, column = 2) 
  
# Exit Button 
Exit1 =  Button(root2, padx = 10, pady = 5, bd = 10, fg = "black", 
                        font = ('times', 15, 'bold'),
                      width = 10, text = "Exit", bg = "SkyBlue3", 
                  command = qExit).grid(row = 7, column = 3) 
  
 
root.mainloop() 