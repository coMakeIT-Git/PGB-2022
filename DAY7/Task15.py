import re 
ip_str = input("Enter the string: ")
# Using isalpha() and isnumeric()
ele = list([i for i in ip_str if i.isnumeric()]) 
  
op_result = "".join(ele)  
print ("Output string is:", op_result)