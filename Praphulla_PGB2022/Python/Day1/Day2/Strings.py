String1 = "Hello"
String2 = "Raphy12345"
String3 = ''
for i in range(len(String1)):
    String3 += String1[i]
    String3 += String2[-i-1]
for j in range(len(String1), len(String2)):
    String3 += String2[-j-1]
print(String3)