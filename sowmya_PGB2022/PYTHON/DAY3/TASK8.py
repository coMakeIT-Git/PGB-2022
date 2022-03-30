
t = list(tuple(map(str,input().split())) for r in range(int(input('enter no of rows : '))))  
print("Original list of tuples:")
print(t)
t.sort(key = lambda x: x[1])
print("\nSorting the List of Tuples:")
print(t)
#Original list of tuples:
#[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
	#Sorting the List of Tuples:
	#[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]