# This is my homework for Python Basics.

# Create list of 100 random numbers from 0 to 1000
import random
randomlist = random.sample(range(0, 1000), 100)
print(randomlist)

# Sort list from min to max (without using sort())
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
    if (i % 2 == 0):
        even.append(i)
    else:
        odd.append(i)

print ("Even List: ", even)
print ("Odd List: ", odd)

# Now let`s calculate average for each list
for i in even:
    def average (even):
        return sum (even)/len(even)

for i in odd:
    def average (odd):
        return sum (odd)/len(odd)

# Print both average result in console
print ("Average of the list even =",  average(even))
print ("Average of the list odd =", average(odd))