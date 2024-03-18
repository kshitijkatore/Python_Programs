t = [1, 2, [3, 4], [6, 7]]
t[2].append(5)
t[3].append(8)
print(t)

# What is the output of the following code?
# a)  (1, 3, [3, 4, 5] , [6, 7, 8])
# b) (1, 2, [3, 4], 5)
# c) (1, 2, [3, 4), 5])
# d) Error: Tuples are immutable.