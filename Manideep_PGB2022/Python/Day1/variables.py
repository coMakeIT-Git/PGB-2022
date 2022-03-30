a=1
b=1.32343
c="adnal"
d=[1,2,3]
e=('a','b','c')
k=True
s=set('aaasfdnnaf')
d1={'a':65,'b':66,'c':67}

print("Integer is {} \n Float is {} \n string is {} \n List is {}\n Tuple is {} \n Boolean is {} \n Set is {} \n Dictionary is {}".format(a,b,c,d,e,k,s,d1))



a=2
b=12312.1213
# c[0]='a'  #errordict_keys(['b', 'c'])
d[1]=2
# e[0]=2     Error
k=False
d1['a']=a
# s[1]='b'  #Error
print("Integer is {} \n Float is {} \n string is {} \n List is {}\n Tuple is {} \n Boolean is {} \n Set is {} \n Dictionary is {}".format(a,b,c,d,e,k,s,d))

print("Immutable Datatypes are int, float, bool, string, unicode, tuple")
print("Mutable Data Types are  list, dict, set ")

c=1
a=[12,123]
b=False
d=set('asndoa')
d1=12.1213123
e={'a':65,'b':66,'c':67}
k='asdm'
s=(2,2,32)
print("Integer is {} \n Float is {} \n string is {} \n List is {}\n Tuple is {} \n Boolean is {} \n Set is {} \n Dictionary is {}".format(c,d1,k,a,s,b,d,e))


a1=112
b1='=comakeit'
# c= a1+b1 #error
a=(str(a1)+b1)

#b=False+"adnao"
b=str(False)+"adnao"
print(b)

#c=[1,2,3]+(1,2) # error
c=[1,2,3]+[(12,123,12)]
print(c)







