#!//usr/bin/python3

class Day1:
    def __init__(self):
        # Define variables for each data type and store respective data
        self.dt_dict = {"key1": "Value1", "key2": "Value2"}
        self.dt_list = [1, 2, 3, 4, 5, 6, "seven"]
        self.dt_integer = 1
        self.dt_string = "hello"
        self.dt_set = {"value1", "value2", "value3"}
        self.dt_tuple = 1, 2, 3, 4, 5, 7, 7
        self.dt_frozenSet = frozenset(self.dt_tuple)
        print("\nInitialized Datatypes : \n")
        print(f"Dictionary : {self.dt_dict}")
        print(f"List : {self.dt_list}")
        print(f"Integer : {self.dt_integer}")
        print(f"String : {self.dt_string}")
        print(f"Set : {self.dt_set}")
        print(f"Tuple : {self.dt_tuple}")
        print(f"FrozenSet : {self.dt_frozenSet}")

    def override(self):
        print("\nOverriding Datatypes : \n")
        over = 1
        print("Initialized variable 'over' as Integer : ")
        print(over)
        over = "Override to String"
        print("Override Integer to String")
        print(over)
        over = [1, 2]
        print("Override String to List")
        print(over)
        over = {"key": "value"}
        print("Override List to Dictionary")
        print(over)
        over = {1, 2, 3}
        print("Override Dictionary to Set")
        print(over)
        over = 4, 5, 6
        print("Override Set to Tuple")
        print(over)

    def datatypes_add(self):
        print("\nAdding Datatypes : \n")
        try:
            a = 1 + "String"
        except Exception as e:
            print("Can't add Integer to String : 1 + 'String'")
        try:
            b = "String" + True
        except Exception as e:
            print("Can't add String to Boolean : 'String' + True")
        try:
            c = [1, 2] + (3, 4)
        except Exception as e:
            print("Can't add List to Tuple : [1, 2] + (3, 4)")

    def mutable_immutable(self):
        # Updating Datatypes
        print("\nList Mutable and Immutable Datatypes : \n")
        self.dt_dict["key1"] = "Value3"
        print(self.dt_dict)
        print("Dictionary is Mutable")
        self.dt_list.append("eight")
        print(self.dt_list)
        print("List is Mutable")
        print(self.dt_integer)
        self.dt_integer += 2
        print("Integer is Immutable")
        print(self.dt_string)
        self.dt_string += " world"
        print(self.dt_string)
        print("String is Immutable")
        print(self.dt_set)
        self.dt_set.add("value4")
        print(self.dt_set)
        print("Set is Mutable")
        try:
            self.dt_tuple.append("9")
        except:
            print("Tuple Is Immutable")
        finally:
            print(self.dt_tuple)
        try:
            self.dt_frozenSet.append(2)
        except:
            print("FrozenSet Is Immutable")

    def list_operations(self):
        print("\nList Operations : \n")
        fruits = ['apple', 'banana', 'cherry']
        cars = ['Ford', 'BMW', 'Volvo']
        print(f"Fruits : {fruits}, Cars : {cars}")
        fruits.append("orange")
        print(f"Appended Fruits : {fruits}")
        fruits_copy = fruits.copy()
        print(f"Copied Fruits to new list : {fruits_copy}")
        fruits_copy.clear()
        print(f"Deleted elements in Fruits list : {fruits_copy}")
        print(f"DCount of cherry in Fruits list : {fruits.count('cherry')}")
        fruits.extend(cars)
        print(f"Added elements in cars list into fruits list : {fruits}")
        fruits.insert(1, "orange")
        print(f"Added 'orange' as second element in fruits list : {fruits}")
        del fruits[1]
        print(f"Deleted 2nd element in fruits list : {fruits}")
        fruits.remove("banana")
        print(f"Removed 'banana' from fruits list : {fruits}")
        fruits = fruits[::-1]
        print(f"Reversed elements in fruits list : {fruits}")
        cars.sort()
        print(f"Sorted cars list : {cars}")

    def string_operations(self):
        print("\nString Operations : \n")
        print(f"String : '{self.dt_string}'")
        string = self.dt_string.upper()
        print(f"Converted string to uppercase : {self.dt_string}")
        string = self.dt_string.lower()
        print(f"Converted string to lowercase : {self.dt_string}")
        print(f"Count of letter 'o' in string : {string.count('o')}")
        print(f"Check if string ends with 'd' : {string.endswith('d')}")
        print(f"Check if all characters in string is alphabet : {self.dt_string.isalpha()}")
        print(string.title())
        print(f"Convert the first character of each word to upper case : {string}")
        print(self.dt_string.capitalize())
        print(f"Convert the first character to upper case : {self.dt_string}")
        print(f'Search the string for a specified value and returns the position of where it was found : {string.find("l")}')
        print(f'Reverse the string with slicing : {string[::-1]}')

    def tuple_operations(self):
        print("\nTuple Operations : \n")
        print(f"Tuple : {self.dt_tuple}")
        print(f"Count of value 7 in Tuple : {self.dt_tuple.count(7)}")
        print(f"Get index of value 3 in Tuple : {self.dt_tuple.index(3)}")

    def dictionary_operations(self):
        print("\nDictionary Operations : \n")
        dict_list = "key1", "key2", "key3"
        print("Create a dictionary with 3 different keys, all with the value '5' using inbuilt method")
        dict1 = dict.fromkeys(dict_list, 5)
        print(f"Dictionary : {dict1}")
        print(f"Return the value of the specified key : {dict1['key1']}")
        print(f"Print all key, value pairs : {dict1.items()}")
        print("Remove the element with the specified key : ")
        del dict1["key2"]
        dict1["key4"] = 6
        print(dict1)
        print("Remove the last inserted key-value pair")
        dict1.popitem()
        print(dict1)

    def set_operations(self):
        print("\nSet Operations  : \n")
        print(f"Set : {self.dt_set}")
        self.dt_set.add(10)
        print(f"Added an element to the set : {self.dt_set}")
        self.dt_set.remove(10)
        print(f"Remove specific element from the set (10): {self.dt_set}")

    def two_sets_operations(self):
        print("\nTwo Sets Operations : \n")
        x = {1, 2, 3, 4, 5, 7}
        y = {6, 7, 8, 9, 10, 11}
        print("Create 2 sets x and y : ")
        print("x = ", x)
        print("y = ", y)
        print(f"Return a set that contains the items that only exist in set x, and not in set y : {x.difference(y)}")
        print("Remove the items that exist in both sets : ")
        x.difference_update(y)
        print(x)
        print(f"Items that exist in both sets : {x.intersection(y)}")
        print(f"Return True if no items in set x is present in set y : {x.isdisjoint(y)}")
        print(f"Return True if all items in set x are present in set y : {x.issubset(y)}")
        print(f"Return True if all items set y are present in set x : {x.issuperset(y)}")
        print(f"Return a set that contains all items from both sets, except items that are present in both sets : {x.symmetric_difference(y)}")
        print(f"Remove the items that are present in both sets, AND insert the items that is not present in both sets : ")
        x.symmetric_difference_update(y)
        print(x)
        print(f"Return a set that contains all items from both sets, duplicates are excluded : {x.union(y)}")
        print("Insert the items from set y into set x : ")
        x.update(y)
        print(x)


main = Day1()
main.override()
main.datatypes_add()
main.mutable_immutable()
main.list_operations()
main.string_operations()
main.tuple_operations()
main.dictionary_operations()
main.set_operations()
main.two_sets_operations()