

------------------------------------------------------------------------------------------------------------------------------------------------------------
All exceptions regarding student info:
AgeNotSufficient Exception: you are underaged
Student added sucessfully
Student added sucessfully
Invalidage Exception: please enter valid age
InvalidMail exception: your mail is not proper
Not Unique Name Exception The name already exists

------------------------------------------------------------------------------------------------------------------------------------------------------------
Caluclator output:
Enter space separated formula:4 - 6
-2.0
Enter space separated formula:5 + 4
9.0
Enter space separated formula: 6 * 3
18.0
Enter space separated formula: 7 / 4
1.0
Enter space separated formula:5 @ 4
Traceback (most recent call last):
  File "/home/localadmin/PGB-2022/kranthi_PGB-2022/PYTHON/day4/simplecalc.py", line 32, in <module>
    result=caluclate(n1,op,n2)
  File "/home/localadmin/PGB-2022/kranthi_PGB-2022/PYTHON/day4/simplecalc.py", line 24, in caluclate
    raise FormulaError('{} it is not a valid operater')
__main__.FormulaError: {} it is not a valid operater


Enter space separated formula:1 2 @ 3
Traceback (most recent call last):
  File "/home/localadmin/PGB-2022/kranthi_PGB-2022/PYTHON/day4/simplecalc.py", line 31, in <module>
    n1,op,n2=parse_input(ur_input)
  File "/home/localadmin/PGB-2022/kranthi_PGB-2022/PYTHON/day4/simplecalc.py", line 6, in parse_input
    raise FormulaError('please enter only 3 separated values')
__main__.FormulaError: please enter only 3 separated values
------------------------------------------------------------------------------------------------------------------------------------------------------------
The number of words in the sentence of the file are:
12
------------------------------------------------------------------------------------------------------------------------------------------------------------

a Python program to remove newline characters from a file 

['This is my file to count numbers of words in it ', 'This is a new line kranthi ', 'This is the third  line kranthi ', 'I am keep on writing my fourth line yaar']

------------------------------------------------------------------------------------------------------------------------------------------------------------
a Python program to copy the contents of a file to another file .
This is my file to count numbers of words in it 
This is a new line kranthi 
This is the third  line kranthi 
I am keep on writing my fourth line yaar



------------------------------------------------------------------------------------------------------------------------------------------------------------
Enter CSV File Name (csvfile.csv) : sample1.csv
Total Number of Rows : 9
Total Number of columns : 13
feild Names : ['Month', ' "Average"', ' "2005"', ' "2006"', ' "2007"', ' "2008"', ' "2009"', ' "2010"', ' "2011"', ' "2012"', ' "2013"', ' "2014"', ' "2015"']
------------------------------------------------------------------------------------------------------------------------------------------------------------
A progrom to insert hash
T#H#E# #W#o#r#l#d# #i#s# #r#o#u#n#d#
------------------------------------------------------------------------------------------------------------------------------------------------------------
Output for custom errors:
Error Name : ZeroDivisionError
Error Message : division by zero
Error Name : ImportError
Error Message : cannot import name 'notexistingmethod' from 're' (/usr/lib/python3.8/re.py)
Error Name : IndexError
Error Message : list index out of range
Enter String : 
Error Name : ValueError
Error Message : invalid literal for int() with base 10: ''
Error Name : CustomException
Error Message : This is an custom Exception
Enter 1st Number : 
Error Name : ValueError
Error Message : invalid literal for int() with base 10: ''
