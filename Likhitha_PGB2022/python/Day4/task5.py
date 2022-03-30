#class ZeroDivisionError(Exception):
 #   pass

# class ImportError(Exception):
#     pass

# class IndexError(Exception):
#     pass

# class IndentationError(Exception):
#     pass

# class ValueError(Exception):
#     pass


try:  
    a = 100 / 0
    print (a)
except ZeroDivisionError:  
        print ("Zero Division Exception Raised." )
else:  
    print ("Success, no error!")
    
    
try:
    import likhitha
    
except ImportError:
    print("Import error is raised")
    
else:
    print ("Success, no error!")
    
try:
    a=[10,20,30]
    print(a[5])
    
except:
    print("IndexError is raised")
    
else:
    print("There is no error")
    
try:
    for i in range(10):
      print(i)
   
except:
    print("Indentation eror is raised")
    
else:
    print("There is no error")
    

try:
    import math
    math.sqrt(-10)
    
except:
    print("value error is raised")
    
else:
    print("No error")
    
finally:
    print("These are some exceptions in python")
    
    
    