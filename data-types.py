# Datatypes in python
# Text type -- str
# Numeric types -- int float complex
# Sequence types --- list tuple range
# Mapping type -- dict
# set types -- st frozenset
# boolean type -- bool
# Binary type -- bytes, bytearray, memoryview
# None type -- NoneType


# Example
x = 5
print(type(x))


# Sequence type
# LIST
s = ["apple", "banana", "cherry"]
print("Printing the list items: ", s, sep='')
print(type(s))

# TUPLE
t = ("apple", "banana", "cherry")
print(t)
print(type(t))
# Since tuples are indexed, they can have items with the same value:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
# To determine how many items a tuple has, use the len() function:
tuple_length = len(thistuple)
print("To determine how many items a tuple has, use the len() function: >>", tuple_length)

# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
oneTuple = ("apple",)
print("tuple with one item should include comma ", type(oneTuple))

oneTuple2 = ("apple")
print("creating single tuple without commma at the end will not recognize it a tuple >>> ", type(oneTuple2))

# Tuple items can be of any data type:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

any_type_tuple = ("appple", 2, 0.45, True, False)

print("printing the tuple of any type: ", any_type_tuple)

for _tuple in any_type_tuple:
    print(_tuple)

# *** USING tuple CONSTRUCTOE *** #

tuple_from_constructor = tuple(("apple", "banana", "gauava"))
print("creating tuple from the constructor", tuple_from_constructor)
