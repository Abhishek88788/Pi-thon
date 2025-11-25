# Creating a frozenset from a list
my_list = [1, 2, 3, 2, 4]
my_frozenset = frozenset(my_list)
print(my_frozenset)

# Creating a frozenset from a tuple
my_tuple = ("apple", "banana", "cherry")
another_frozenset = frozenset(my_tuple)
print(another_frozenset)

# Creating an empty frozenset
empty_frozenset = frozenset()
print(empty_frozenset)

# Demonstrating immutability
try:
    my_frozenset.add(5)
except AttributeError as e:
    print(f"Error: {e} - frozensets are immutable and do not support item addition.")
# Demonstrating that frozensets are hashable and can be used as dictionary keys
my_dict = {my_frozenset: "This is a frozenset key"}
print(my_dict)# Demonstrating set operations with frozensets
set_a = frozenset([1, 2, 3])
set_b = frozenset([3, 4, 5])