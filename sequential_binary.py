from math import floor

class SequentialStringList(list):

    def __init__(self):
        self.items = []

    def add(self, item):
        # that when given a string, it adds it to
        # an internal list object. You can use the
        # list object from the standard python library for the internal list
        self.append(item)

    def find(self, item):
        pos = 0
        while pos < len(self):
            if self[pos] == item:
                return pos
            else:
                pos = pos + 1
        return None

class BinaryStringList(list):

    def add(self, item):
        #print("here")
        self.append(item)

    def find(self, item):

        length = len(self)
        left = 0
        right = length - 1

        while left <= right:
            middle = floor((left + right)/2)
            if self[middle] < item:
                left = middle + 1
            if self[middle] > item:
                right = middle - 1
            elif self[middle] == item:
                print("found")
                return middle

        print("not found")
        return None


