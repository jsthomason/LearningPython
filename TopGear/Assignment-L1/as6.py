#!/usr/bin/python3

#
# Python Assignment #6
# filename: as6.py
#

import sys

#
# 6. Write a function to print the information in the dictionary(bookstore) in the given format
# 
# bookstore={"New Arrivals":{
#            "COOKING":["Everyday Italian","Giada De Laurentiis","2005","30.00"],
#            "CHILDREN":["Harry Potter”, J K. Rowling","2005","29.99"],
#            "WEB":["Learning XML","Erik T. Ray","2003","39.95"]
#            }
#           }
# 
# 
# BOOKSTORE
# 
# 'Learning XML', 'Erik T. Ray', '2003', '39.95' 
# 'Everyday Italian', 'Giada De Laurent is', '2005', '30.00'
# 'Harry Potter', 'J K. Rowling', '2005', '29.99'
# 

bookstore={
            "New Arrivals":{
                "COOKING":['Everyday Italian','Giada De Laurentiis','2005','30.00'],

                "CHILDREN":['Harry Potter', 'J K. Rowling','2005','29.99'],

                "WEB":['Learning XML','Erik T. Ray','2003','39.95']
                }
           }

def fmtNewArrivals(dic):
    for genre, book in dic["New Arrivals"].items():
        print("{!r}, {!r}, {!r}, '${!s}'".format(book[0], book[1], book[2], book[3]))

print("\nPython Assignment #6")

print("\nBOOKSTORE\n")
fmtNewArrivals(bookstore)
print()

sys.exit(0)
