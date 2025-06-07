file = open("test.txt", 'r')

# Read all the contents of file
#print(file.read(25))

# use readline() to print each line of the file
line = file.readline()
while line != "":
    print(line)
    line = file.readline()

file.close()

print("*****************")

new_file = open("test.txt", 'r')

lines = new_file.readlines()
for line in lines:
    print(line.strip())

new_file.close()

# Write to files using sample steps below
# For this exercise - read the file and store each line in a list
# Reverse the list
# Write the list back to the file
with open("test.txt", 'r') as f:
    content = f.readlines()
    for line in content:
        line.strip()
    reversed_list = reversed(content)
    with open("test.txt", 'w') as writer:
        for line in reversed_list:
            writer.write(line)
