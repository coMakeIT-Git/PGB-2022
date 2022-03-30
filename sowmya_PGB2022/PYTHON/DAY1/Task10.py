#TASK10

#Return the value of the specified key
marks = {'Physics':67, 'Maths':87}
print(marks.get('Physics'))


#Print all key, value pairs
a_dictionary = {"a": 1, "b": 2}
for pair in a_dictionary.items():

    print(pair)

# Dictionary of strings and int
word_freq_dict = {"Hello": 56,"at": 23,"test": 43,}
key_to_be_deleted = 'at'
new_dict = {}
for key, value in word_freq_dict.items():
    if key is not key_to_be_deleted:
        new_dict[key] = value
word_freq_dict = new_dict
print(word_freq_dict)

#Remove the last inserted key-value pair
marks = {'Physics':67, 'Maths':87}
marks.popitem()
print(marks)