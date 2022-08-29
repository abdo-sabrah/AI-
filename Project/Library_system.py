#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Library  :
    lendlist = {}
    def __init__ (self,listofbooks,library_name):
        self.listofbooks= listofbooks
        self.library_name=library_name
        Library.lendlist
#display all library books
    def Displaybook(self):
        print(f"the available books is {self.listofbooks}")
        
    def lendbook(self,book_name):
        
        name=input("please enter your name ")
        self.lendlist [name] =book_name  
        
#removig book after lending
        for i in self.listofbooks :
            self.listofbooks.remove(i)
        print ("plz return the book in the deadline")
        
#method to display lend list
    def get_lendlist(self):
        return print (f"the lend list is  {self.lendlist}")
    
#method to add a book in the library
    def Addbook (self,new_book_name):
        self.listofbooks.append(new_book_name)
        
#method return the lend books
    def Returnbook (self,Rbook_name):
         for Rbook_name in self.lendlist:
            self.Addbook(Rbook_name)
            
#creating the library
Harrylibrary =Library (["100","good g","my way","nat GEO","deep","The MOOn"],"PHARAOH")

print("hi, how can i help you ? ")
while True :
    Answer = input()
    if Answer.lower() == "display":
        
        Harrylibrary.Displaybook()
        
    if Answer.lower() == "lend book":
        book_name = input ("please enter book name")
        
        Harrylibrary.lendbook(book_name)
    
    
    if Answer.lower() == "add book":
        new_book_name = input ("enter book name you want to add")
        Harrylibrary.Addbook (new_book_name)
    
    if Answer.lower() == "return book":
        Rbook_name = input ("thanks a lot :) what is book name you want to return")
        Harrylibrary.Returnbook (Rbook_name)





# In[ ]:





# In[ ]:




