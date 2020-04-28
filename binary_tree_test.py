import timeit
from binary_tree import BinaryTree
nums = [8, 99, 14, 7, 54, 9]
binary = BinaryTree(22)

print("Fill List with numbers")
for i in range(len(nums)):
    binary.insert(nums[i])
t = timeit.Timer("BinaryTree: binary.find(5)", "from binary_tree import BinaryTree").timeit()
t2 = timeit.Timer("BinaryTree: binary.find(14)", "from binary_tree import BinaryTree").timeit()
print("The search took", t, " seconds ")
print("The search took", t2, " seconds ")


