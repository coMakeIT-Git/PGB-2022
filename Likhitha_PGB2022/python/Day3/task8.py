
#Python program to sort a list of tuples using Lambda

subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

print("Original list of tuples:")
print(subject_marks)
#lambda expression
subject_marks.sort(key = lambda x: x[1])

print("\nSorting the List of Tuples:")
print(subject_marks)
