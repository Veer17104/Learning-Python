# type conversion in implicit, that is python interpreter will automatically perform these for us.

a = 9
b = 5
print(a/b) # converts to a float value
print(type(a/b)) # float

print(type(5 + 10.0)) # float


# type casting is explicit, which is done by the developer and can only be done among compatible data types
# we use these functions --> int(), float(), bool() etc

a = 10
print(float(a))
print(bool(a))