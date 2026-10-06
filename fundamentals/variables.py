# Variables are basically storage containers to store data
# Basically what happens is our computer has memory containers. 
# Each container is of 8 bits or say 1 byte.
# These variables are used as references pointing to ab object.

x = 10 # creates and [int : 10] object in memory and x points to it
print(x) #10
y = x # now y is also pointing to the same int : 10 object
print(y) #10
x = 20 # now a new [int : 20] object is created and x points to it

print(x) # 20 
print(y) # 10 because y still points to 10.