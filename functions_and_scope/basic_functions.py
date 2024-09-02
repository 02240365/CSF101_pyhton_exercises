#1
def greet():
    print("Hello, World!")

greet()

#2
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

#3
def square(number):
    return number ** 2

result = square(5)
print(result)

#4
def is_even(number):
    return number % 2 == 0

print(is_even(4))
print(is_even(7))

#5
def print_numbers(n):
    for i in range(1, n + 1):
        print(i)

print_numbers(5)
