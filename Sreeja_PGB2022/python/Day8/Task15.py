test_list = [('red ', 'pink'), ('white ', 'black'), ('orange ', 'green')]
  
# printing the original list
print ("The original list is : " + str(test_list))
  
# using list comprehension + join()
# conversion of list of tuple to list of list 
res = [''.join(i) for i in test_list] 
# printing result
print ("The list of tuples after converting to list of string : " + str(res))