# In Python, a function is a group of related statements that perform a specific task

# Function declaration
def greetme(name):
    print(f"Good Morning, {name}!")

def add_integers(a, b):
    return a + b

# Function Call
my_name = input("Enter your name: ")
greetme(my_name)

first_number = int(input("Enter your first number: "))
second_number = int(input("Enter your second number: "))
print(f"{first_number} + {second_number} = {add_integers(first_number, second_number)}")
