#tuple operations
tp=("ab","abc","abcd","abcd","abc")
print("element abc occured:",tp.count("abc"))
print("element abc occured at position:",tp.index("abc"))

#dictionary with 3 different keys, all with the value '5' using inbuilt method

x = ('key1', 'key2', 'key3')
y = 5

thisdict = dict.fromkeys(x, y)

print(thisdict)
#Dictionary operations
mydict={"reethu":20,"lucky":30,"dimple":50,"riya":70}
print("value of reethu:",mydict.get("reethu"))
print("Keyvalue pairs are:",mydict)
result=mydict.pop("reethu")
print("Dictionary after removing element", mydict)
result=mydict.popitem()
print("Dictionary after removing last inserted keyvalue pair",mydict)

#set operations
st={1,2,3,4}
st.add(5)
print("set after adding element 5:",st)
st.remove(4)
print("set after removing element 4:",st)

x={1,2,3,4,5,6}
y={1,2,6}
result=x.difference(y)
print("Elements that exist in x but not in y are:",result)
print("Sets after removing common elements :")
res=set(x).difference(y)
print(res)
ans=set(y).difference(x)
print(ans)
res=x.isdisjoint(y)
print("no items in set x is present in set y",res)
res=x.issubset(y)
print("all items in set x are present in set y",res)
res=y.issubset(x) 
print("items set y are present in set x:",res)
res=x.symmetric_difference(y)
print("set that contains all items from both sets, except items that are present in both sets:",res)
res=x.symmetric_difference_update(y)
print("Remove the items that are present in both sets, AND insert the items that is not present in both sets",res)
res=x.union(y)
print("a set that contains all items from both sets, duplicates are excluded:",res)
res=x.update(y)
print("Insert the items from set y into set x",res)
