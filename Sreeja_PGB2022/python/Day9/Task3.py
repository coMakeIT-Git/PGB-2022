def count_words(file):
   with open('Day9/file1.txt','r+') as f:
       data = f.read()
       data.replace(",", " ")
       return len(data.split(" "))
print(count_words("Day9/file1.txt"))

