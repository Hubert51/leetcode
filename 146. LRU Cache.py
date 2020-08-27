class Node:
    def __init__(self, key, prevKey, nextKey):
        self.key = key
        self.prevKey = prevKey
        self.nextKey = nextKey

    def setPrevKey(self, prevKey):
        self.prevKey = prevKey

    def setNextKey(self, nextKey):
        self.nextKey = nextKey


class LRUCache:

    def __init__(self, capacity: int):
        self.keyDict = dict()
        self.priorityDict = dict()
        self.lowestPriorityKey = 0
        self.highestPriorityKey = 0
        self.capacity = capacity
        self.current = 0

    def get(self, key: int) -> int:
        if key in self.keyDict:
            value = self.keyDict[key][0]
            self.put(key, value)
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # print(key, value)
        # base case
        if self.current == 0:
            self.keyDict[key] = (value, self.highestPriorityKey)
            keyNode = Node(key, -1, -1)
            self.priorityDict[self.highestPriorityKey] = keyNode
            self.current += 1
            return

        # increase the priority and update the value
        if key in self.keyDict:
            priorityNum = self.keyDict[key][1]

            # only one element in the cache
            if self.lowestPriorityKey == self.highestPriorityKey:
                self.keyDict[key] = (value, self.highestPriorityKey)

            # if the key has highest priority, only update the value in the cache
            elif priorityNum == self.highestPriorityKey:
                self.keyDict[key] = (value, self.highestPriorityKey)

            else:
                self.update(key, value)

        else:
            if self.current == self.capacity:
                self.highestPriorityKey += 1
                self.keyDict[key] = (value, self.highestPriorityKey)
                self.priorityDict[self.highestPriorityKey] = Node(key, self.highestPriorityKey - 1, -1)
                self.priorityDict[self.highestPriorityKey - 1].setNextKey(self.highestPriorityKey)

                keyNode = self.priorityDict[self.lowestPriorityKey]
                oldPriorityKey = self.lowestPriorityKey

                self.lowestPriorityKey = keyNode.nextKey
                self.priorityDict[self.lowestPriorityKey].setPrevKey(-1)

                # romve the least priority item
                self.keyDict.pop(keyNode.key)
                self.priorityDict.pop(oldPriorityKey)

            else:
                self.highestPriorityKey += 1
                self.keyDict[key] = (value, self.highestPriorityKey)
                self.priorityDict[self.highestPriorityKey] = Node(key, self.highestPriorityKey - 1, -1)
                self.priorityDict[self.highestPriorityKey - 1].setNextKey(self.highestPriorityKey)
                self.current += 1

    def update(self, key, value):
        oldPriority = self.keyDict[key][1]
        oldKeyNode = self.priorityDict[oldPriority]

        #### IMPORTANT: need to check whether the current one is the lowest priority
        if oldPriority == self.lowestPriorityKey:
            self.lowestPriorityKey = oldKeyNode.nextKey

        if oldKeyNode.prevKey != -1:
            self.priorityDict[oldKeyNode.prevKey].setNextKey(oldKeyNode.nextKey)
        if oldKeyNode.nextKey != -1:
            self.priorityDict[oldKeyNode.nextKey].setPrevKey(oldKeyNode.prevKey)

        self.priorityDict.pop(oldPriority)

        newKeyNode = Node(key, self.highestPriorityKey, -1)

        self.highestPriorityKey += 1
        self.priorityDict[self.highestPriorityKey - 1].setNextKey(self.highestPriorityKey)
        self.priorityDict[self.highestPriorityKey] = newKeyNode
        self.keyDict[key] = (value, self.highestPriorityKey)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == '__main__':
    a = [ "put", "put", "put", "put", "put", "get", "put", "get", "get", "put", "get", "put", "put", "put",
     "get", "put", "get", "get", "get", "get", "put", "put", "get", "get", "get", "put", "put", "get", "put", "get",
     "put", "get", "get", "get", "put", "put", "put", "get", "put", "get", "get", "put", "put", "get", "put", "put",
     "put", "put", "get", "put", "put", "get", "put", "put", "get", "put", "put", "put", "put", "put", "get", "put",
     "put", "get", "put", "get", "get", "get", "put", "get", "get", "put", "put", "put", "put", "get", "put", "put",
     "put", "put", "get", "get", "get", "put", "put", "put", "get", "put", "put", "put", "get", "put", "put", "put",
     "get", "get", "get", "put", "put", "put", "put", "get", "put", "put", "put", "put", "put", "put", "put"]
    b = [[10, 13], [3, 17], [6, 11], [10, 5], [9, 10], [13], [2, 19], [2], [3], [5, 25], [8], [9, 22], [5, 5],
     [1, 30], [11], [9, 12], [7], [5], [8], [9], [4, 30], [9, 3], [9], [10], [10], [6, 14], [3, 1], [3], [10, 11], [8],
     [2, 14], [1], [5], [4], [11, 4], [12, 24], [5, 18], [13], [7, 23], [8], [12], [3, 27], [2, 12], [5], [2, 9],
     [13, 4], [8, 18], [1, 7], [6], [9, 29], [8, 21], [5], [6, 30], [1, 12], [10], [4, 15], [7, 22], [11, 26], [8, 17],
     [9, 29], [5], [3, 4], [11, 30], [12], [4, 29], [3], [9], [6], [3, 4], [1], [10], [3, 29], [10, 28], [1, 20],
     [11, 13], [3], [3, 12], [3, 8], [10, 9], [3, 26], [8], [7], [5], [13, 17], [2, 27], [11, 15], [12], [9, 19],
     [2, 15], [3, 16], [1], [12, 17], [9, 1], [6, 19], [4], [5], [5], [8, 1], [11, 7], [5, 2], [9, 28], [1], [2, 2],
     [7, 4], [4, 22], [7, 24], [9, 26], [13, 28], [11, 26]]

    obj = LRUCache(10)
    for i in range(len(a)):
        print(a[i], b[i])
        if a[i] == "put" and b[i] == [5,18]:
            print(1)
        if a[i] == "put":
            obj.put(b[i][0], b[i][1])

        else:
            obj.get(b[i][0])

