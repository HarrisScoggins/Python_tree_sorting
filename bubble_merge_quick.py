from math import floor


class BubbleStringList(list):

    def __init__(self):
        self.items = []

    def add(self, item):
        self.append(item)

    def sort(self):
        l = len(self)

        for i in range(l):
            for j in range(0, l - i - 1):
                if self[j] > self[j + 1]:
                    self[j], self[j + 1] = self[j + 1], self[j]


class MergeStringList(list):

    def __init__(self):
        self.items = []

    def add(self, item):
        self.append(item)

    def merge(self, left, right):

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                self[k] = left[i]
                i = i + 1
            else:
                self[k] = right[j]
                j = j + 1
            k = k + 1
        while i < len(left):
            self[k] = left[i]
            i = i + 1
            k = k + 1
        while j < len(right):
            self[k] = right[j]
            j = j + 1
            k = k + 1

    def merge_sort(self):
        n = len(self)
        if n < 2:
            return

        mid = int(n / 2)
        left = MergeStringList()
        right = MergeStringList()

        for i in range(mid):
            number = self[i]
            left.append(number)

        for i in range(mid, n):
            number = self[i]
            right.append(number)

        right.merge_sort()
        left.merge_sort()

        self.merge(left, right)

class QuickStringList(list):

    def add(self, item):
        self.append(item)

    def partition(arr, low, high):
        i = low - 1
        pivot = arr[high]
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[j], arr[i] = arr[i], arr[j]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quickSort(arr, low, high):
        if low >= high:
            return
        p = QuickStringList.partition(arr, low, high)
        QuickStringList.quickSort(arr, low, p - 1)
        QuickStringList.quickSort(arr, p + 1, high)


class test:

    import timeit
    from bubble_merge_quick import BubbleStringList
    from bubble_merge_quick import MergeStringList
    from bubble_merge_quick import QuickStringList
    list1 = [45, 87, 4, 5, 88, 1, 44]
    list2 = BubbleStringList()
    for i in range(len(list1)):
        list2.add(list1[i])
    t = timeit.Timer("BubbleStringList: list2.sort()", "from bubble_merge_quick import BubbleStringList").timeit()
    print(t, "time for bubble sort ")



    merge = MergeStringList()
    for i in range(len(list1)):
        merge.add(list1[i])

    length = int(len(merge))
    #merge.merge_sort()
    t2 = timeit.Timer("MergeStringList: merge.merge_sort()", "from bubble_merge_quick import MergeStringList").timeit()
    print(t2, "time for merge sort ")


    quick = QuickStringList()
    for i in range(len(list1)):
        quick.add(list1[i])
    #quick.quickSort(0, len(quick) - 1)
    t3 = timeit.Timer("QuickStringList: quick.quickSort(0, len(quick) - 1)", "from bubble_merge_quick import QuickStringList").timeit()
    print(t3, "time for quick sort")

test()