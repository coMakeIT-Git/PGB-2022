str=input("Enter the String :")
let=dig=special=0

for i in range(len(str)):
    if str[i].isalpha():
        let+=1
    elif str[i].isdigit():
        dig+=1
    else:
        special+=1
        
print("\n Number of letters in given string :",let)
print("Number of digits in given string :",dig)
print("Number of special characters in string :",special)            
             
        
    
