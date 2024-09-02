#11
x = 10
def print_x():
    x = 20
    print(f"Local x: {x}")

print_x()
print(f"Global x: {x}")

#12
count = 0

def increment():
    global count
    count += 1
    print (f"Count: {count}")

increment()
increment()
print(f"Final count: {count}")

#13
def outer():
    x = "outer"

    def inner():
        nonlocal x
        x = "inner"
        print(f"Inner x: {x}")

    inner()
    print(f"Outer x: {x}")

outer()
