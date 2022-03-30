#TASK5

#int and string concatenation
a=1
b="string2"
#c=a+b#TypeError:unsupported operand type(s) for +: 'int and 'str'
c=str(a)+b #solution
print(c)#prints 1string2

#string and boolean concatenation
string = "saisowmya"
boolean = True
#str_bool_concat=string+boolean #TypeError;can only concatenate str (not "bool") to str
str_bool_concat= string + str(boolean) #solution
print(str_bool_concat) #prints saisowmyaTrue

#list and tuple concatenation
list_ele=[1,2,3,4]
tup_ele=(5,6,7)
#list_tup_concat=list_ele+tup_ele #TypeError: can only concatenate list (not "tuple") to list
print(list_ele+list(tup_ele))