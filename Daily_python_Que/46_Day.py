def func(x, y=[4,2]):
    y.append(x)
    return y

print(func(1,[3,2]))

# what is the output of this code?  
# a)[4, 2, 1]
# b)[3, 2, 1]
# c)[4, 2, 1, 3, 2]
# d)None