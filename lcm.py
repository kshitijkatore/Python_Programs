# Program to compute LCM

def compute_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while(True):
        if((greater % x == 0) and (greater % y== 0)):
            lcm = greater
            break
        greater += 1
    return lcm

num1 = int(input("Enter the greater number :"))
num2 = int(input("Enter the smaller number :"))

print("The L.C.M is", compute_lcm(num1, num2))