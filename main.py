# This is my homework for Python Basics.

# Create list of 100 random numbers from 0 to 1000
import random
randomlist = random.sample(range(0, 1000), 100)
print(randomlist)

# Sort list from min to max (without using sort())
# With help of two loops we can rearrange the numbers in the sequence using formula below.
# With the first loop each number in randomlist is compared with '1'.
# If there is any number in the sequence which is less than '1' it will be placed on the first place in the new sequence.
# Next loop will compare all numbers to '2' and so on.
for i in range(len(randomlist)):
    for j in range(i + 1, len(randomlist)):

        if randomlist[i] > randomlist[j]:
            randomlist[i], randomlist[j] = randomlist[j], randomlist[i]
print(randomlist)

# Calculate average for even and odd numbers
# First let`s create two separate lists for even and odd numbers
even = []
odd = []
for i in randomlist:
    if i % 2 != 0:
        odd.append(i)
    else:
        even.append(i)

print("Even List: ", even)
print("Odd List: ", odd)

# Now let`s calculate average for each list
for i in even:
    def average(even):
        return sum(even)/len(even)

for i in odd:
    def average(odd):
        return sum(odd)/len(odd)

# Print both average result in console
print("Average of the list even =",  average(even))
print("Average of the list odd =", average(odd))