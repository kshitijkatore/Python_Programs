def sum(num):
    if num == 1:
        return 1
    return num + sum (num - 1)
print(sum(5))

# What is the output of the above code?
# A.1
# B.5
# C.10
# D.15