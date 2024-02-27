data = [1, 2, 3, 4]
backup_data = data.copy()
data[3] = 7
print(backup_data)

# what is the output of the following code?
# A. [1, 2, 3, 4]
# B. [1, 2, 3, 7]
# C. [7, 2, 3, 4]
# D. [1, 2, 7, 4]