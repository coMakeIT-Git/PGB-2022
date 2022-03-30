
#Given two strings, s1 and s2. Write a program to create a new string s3 made
#of the first char of s1, then the last char of s2, Next, the second char of s1 and second last char of s2, and so on.
#left over joins at the end

def merge(s1,s2):
    s_result=""
    i=0
    while(i<len(s1) or i<len(s2)):
        if(i<len(s1)):
            s_result+=s1[i]
        if(i<len(s2)):
            s_result+=s2[len(s2)-1-i]
        i+=1
    return s_result
print("Function to print merged string with given conditions:")
print(merge('kranthi','vijay'))

