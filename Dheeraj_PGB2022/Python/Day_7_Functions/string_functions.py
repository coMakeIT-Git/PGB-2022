import string


class StringsFunctions:

    def __init__(self):
        self.count_all("/*We are le@arning python@67 fun_da**mentals**")

        self.concat_strings("abcdef", "xyz123")

        self.remove_punc("/*We are le@arning python@67 fun_da**mentals**")

        self.only_digit("I am 20 years and and 22 months old")

        self.alpha_num("Sriman25 is Data scientist50 and AI Expert")

    # Count all letters, digits, and special symbols from a given string
    def count_all(self, string):
        a, d, s = 0, 0, 0
        for i in string:
            if i.isalpha():
                s += 1
            elif i.isdigit():
                d += 1
            else:
                a += 1

        print(a, d, s)
        return a, d, s

    # Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.
    def concat_strings(self, s1, s2):
        s3 = ""
        for i, j in zip(s1, s2[::-1]):
            s3 += i + j
        print(s3)
        return s3

    # Write a program to remove special symbols / punctuation from a string
    # 	Ex : str1 = "/*We are le@arning python@67 fun_da**mentals**"
    # 	Output: We are learning python fundamentals
    def remove_punc(self, s):
        output = s.translate(str.maketrans('', '', string.punctuation))
        print(output)
        return output

    # Write a program to removal all characters from a string except integers
    # 	Input : str1 = 'I am 20 years and and 22 months old'
    # 	Output : 2022
    def only_digit(self, s):
        output = s.translate(str.maketrans('', '', string.ascii_letters + string.punctuation + " "))
        print(output)
        return output

    # Write a program to find words with both alphabets and numbers from an input string.
    # 	Input : str1 = "Sriman25 is Data scientist50 and AI Expert"
    # 	Output : ['Sriman25','Scientist50']
    def alpha_num(self, s):
        l = []
        for i in s.split():
            if i.isalnum() and not (i.isalpha() or i.isdigit()):
                l.append(i)

        print(l)
        return l


run = StringsFunctions()