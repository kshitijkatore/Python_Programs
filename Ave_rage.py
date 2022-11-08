def Ave_rage(a, b):
    """ Thise is the function which will calculate average of two numbers"""
    average = (a+b)/2
    return average

a = int(input("Enter the first number :"))
b = int(input("Enter the second number :"))
print(Ave_rage(a, b))
print(Ave_rage.__doc__)