import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure
duplicates2 = {}

# base: this is O(n^2)

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# mvp: this is o (n log n)

# bst = BinarySearchTree(names_1[0])
# count = 0
# for name in names_1:
#     if count == 0:
#         count += 1
#     else:
#         bst.insert(name)

# for name in names_2:
#     if bst.contains(name):
#         duplicates.append(name)

# stretch: O(n)

for name in names_1:
    duplicates2[name] = 1

for name in names_2:
    if name in duplicates2:
        duplicates2[name] += 1

for k, v in duplicates2.items():
    if v > 1:
        duplicates.append(k)

# stretch 2: arrays only



end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
