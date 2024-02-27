def calc(*args):
    count = len(args)
    elem = args[count - 1]
    return count * elem

print(calc(2,2,1,3))

# What is the output of the following code?
# A. 4
# B. 8
# C. 12
# D. Error