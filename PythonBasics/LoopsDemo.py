
greeting = "Good Morning"

if greeting == "Good Morning":
    print("Condition Matches")
    print("second line")
else:
    print("Condition Not Matched")

print("If-else condition code is complete.")

numbers = [2, 3, 5, 7, 9]

for number in numbers:
    print(number)

print()

# print the sum of the First Five Natural Numbers -> 1+2+3+4+5 = 15
# range(i,j) -> i to j-1
total = 0
for j in range(1,6):
    total += j
print(total)

# setting step value in for loop
print("************************************")
for k in range(1,10,2):
    print(k)

it = 4
print("************************************")
while it > 1:
    if it == 3:
        break
    print(it)
    it -= 1

num = 5
print("************************************")
while num > 1:
    if num == 3:
        num -= 1
        continue

    print(num)
    num -= 1
