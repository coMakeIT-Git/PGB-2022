def display_student(name, age):
    print(name, age)

# call using original name
display_student("sowmya", 26)

# assign new name
showStudent = display_student
# call using new name
showStudent("sowmya", 26)