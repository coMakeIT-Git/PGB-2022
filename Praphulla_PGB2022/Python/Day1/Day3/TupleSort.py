subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print("\n List of Subjects and respective Marks:")
print(subject_marks)
subject_marks.sort(key = lambda x: x[1])
print("\n Sorting the List of Tuples based on the Marks:")
print(subject_marks)