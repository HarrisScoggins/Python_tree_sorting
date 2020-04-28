import timeit
from sequential_binary import SequentialStringList


test_strs = ["frank", "tom", "james", "harris", "albert", "adam", "john","ss","str", "yes", "no","code","python", "dog", "cat", "lion", "thee","the","know","no"]

list1 = SequentialStringList()


for e in range(len(test_strs)):
    list1.add(test_strs[e])

print(list1.find("ss"))
t = timeit.Timer("SequentialStringList: list1.find('ss')", "from sequential_binary import BinaryStringList").timeit()
print("To find a item in the list took: ", t ," seconds ")
print(list1.find("frk"))
t2 = timeit.Timer("SequentialStringList: list1.find('frk')", "from sequential_binary import BinaryStringList").timeit()
print("To find a item not in the list took: ", t ," seconds ")
