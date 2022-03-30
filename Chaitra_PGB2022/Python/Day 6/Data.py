#Numeric
n1 = 14
n2 = 14.07
n3 = 26 + 14j
n4 = 24

#Sequence
s1 = "Luna"
s2 = ["Luna", "Lovegood", 1, 2]
s3 = ("Harry", "Ginny", 4)
s4 = "Override"

#Booolean
b1 = True
b2 = False

#Set
s = set(["Luna", "Harry", 1, 3])

#Dictionary
d = {'One':1, 2:'Two', 3:[1,2,3]}

#Overiding
n4 = "hello"
s4 = 5

#Mutability
try:
    n1 = n1+ n2
    print("Numeric types are mutable")
    #s1[2] = s
    s2[2] = 100
    #s3[0] = 999
    print("String and tuple are immutable. Lists are mutable.")
    b2 = True
    print("Boolean types are mutable")
    d[2] = 'Three'
    print("Dictionary types are mutable")
    #s[1] = 1
    print("Sets are immutable.")
except(TypeError):
    print("Immutable")

