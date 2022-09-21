numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# variable to store the sum
sum = 0

# iterate over the list
for val in numbers:
    sum = sum+val

print("The sum is", sum)

##########
# The range() function examples
print(range(10))

print(list(range(10)))

print(list(range(2, 8)))

print(list(range(2, 20, 3)))

################

genre = ["jazz", "pop", "rock"]

# iterate over the list using index
for i in range(len(genre)):
    print("I like", genre[i])

#####
# for with else block

digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left.")


