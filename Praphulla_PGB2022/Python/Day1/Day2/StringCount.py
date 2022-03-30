def Count(str):
    alpha, digit, special = 0, 0, 0
    for i in range(len(str)):
        if str[i].isalpha():
            alpha += 1
        elif str[i].isdigit():
            digit += 1
        else:
            special += 1
    print("\n Printing the string:", str)
    print('Alphabets:', alpha)
    print('Numbers:', digit)
    print('Special characters:', special)
str = "Praphulla1002#$dhhjhd"
Count(str)