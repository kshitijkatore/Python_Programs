def outer():
    x = 10
    def inner():
        nonlocal x
        x += 5
        print("Inner:", x)
    inner()
    print("Outer:", x)
outer()

# What is the output of the follwing code ?
# Inner: 15 Outer: 15
# Inner: 15 Outer: 10
# Inner: 10 Outer: 15
# Error: 