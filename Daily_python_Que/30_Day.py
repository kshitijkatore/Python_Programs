import re

x = re.compile(r'\W')
y = x.findall('clocoding')
print(y)

# What is the output of the following code?
# A. ['c', 'l', 'o', 'd', 'i', 'n', 'g']
# B. []
# c. Error
# D. [' ']