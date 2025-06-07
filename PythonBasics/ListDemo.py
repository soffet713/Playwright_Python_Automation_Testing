
values = [1, 2, "rahul", 4, 5]
# List is a data type that allows multiple values and different data types to be added

print(values[0]) # Should print 1
print(values[3]) # Should print 4
print(values[-1]) # Should print 5 - the last value in the array

for value in values:
    print(value)

values.insert(3, "shetty")
print(values)

values.append("End")
print(values)

values[2] = "RAHUL"
del values[0]
print(values)

# Tuple examples below
values_tuple = (1, 2, "rahul", 4.5)
print(values_tuple)

# Dictionary Example
values_dict = {1: "First Name", 2: "Last Name", "age":33}
print(values_dict[1])
print(values_dict[2])
print(values_dict["age"])

for (key, value) in values_dict.items():
    if type(value) == str:
        print(key, value.upper())
    else:
        print(key, value)

# create dictionary at run time and add values
dict1 = {} # first create an empty dictionary

dict1["firstname"] = "Rahul" # For each value to add to the dictionary, assign it to a new key value in brackets
dict1["lastname"] = "Shetty"
dict1["gender"] = "Male"
print(dict1)
