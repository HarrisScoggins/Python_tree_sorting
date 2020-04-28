from sequential_binary import BinaryStringList
import timeit
test_strs = ["frank", "tom", "james", "harris", "albert", "adam", "john","ss","str", "yes", "no","code","python", "dog", "cat", "lion", "thee","the","know","no"]

list1 = BinaryStringList()

for e in range(len(test_strs)):
    list1.add(test_strs[e])
list1.sort()

print(list1.find("frank"))
t = timeit.Timer("BinaryStringList: list1.find('frank')", "from sequential_binary import BinaryStringList").timeit()
print("To find a item in the list took: ", t ," seconds ")
print(list1.find("apple"))
t2 = timeit.Timer("BinaryStringList: list1.find('apple')", "from sequential_binary import BinaryStringList").timeit()
print("To find a item not in the list took: ", t2 ," seconds ")

