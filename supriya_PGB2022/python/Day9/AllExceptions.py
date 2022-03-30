#Write a class to handle below exceptions
#a. ZeroDivisionError
#b. ImportError
#c. IndexError
#d. IndentationError
#e. ValueError
#f. Exception
#g. Raise any exception and handle it properly and use else, finally blocks to print something irrespective of exception
import math
import sys
class AllException(Exception):
 try:  
    a = 100/0
    print (a)
    
 except ZeroDivisionError:  
        print ("Zero Division Exception Raised." )
 else:  
    print ("Success, no error!")
 try:
    import defg
 except ImportError:
    print("Import error is raised")
 else:
    print("valid import")
 try:
    place=["Hyderabad","Chennai"]
    print(place[5])
 except IndexError:
    print("Index  out of range error raised")
 else:
    print("no error ")
 try:
    import Indent
 except:
     print("Indentation error raised")
 else:
     print("no error")  
 try:
    print(math.sqrt(-4))
 except ValueError:
    print('Value error raised ')  
 else:
     print("Valid value")   

 