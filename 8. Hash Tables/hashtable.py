"""
File: hashtable.py

Case study for Chapter 11.

# TODO ADD THE get AND remove METHODS
get will take the item requested as the parameter and will return the index of the item requested if the item is
found in the table; otherwise will return -1 for item not found

remove mehtod will take the item requested as the parameter and will return true, if the item requested is removed;
otherwise, the method will return -1 for item not found
"""

from arrays import Array

class HashTable(object):
    "Represents a hash table."""

    EMPTY = None
    DELETED = True

    def __init__(self, capacity = 29,
                 hashFunction = hash,
                 linear = True):
        self._table = Array(capacity, HashTable.EMPTY)
        self._size = 0
        self._hash = hashFunction
        self._homeIndex = -1
        self._actualIndex = -1
        self._linear = linear
        self._probeCount = 0
        self.capacity = capacity

    def __len__(self):
        return self._size

    def __str__(self):
        """returns the string representation of the tables array... empty cells show up as None. cells that have prev
        been occupied appear as True"""
        pass

    def insert(self, item):
        """Inserts item into the table
        Preconditions: There is at least one empty cell or
        one previously occupied cell.
        There is not a duplicate item."""
        self._probeCount = 0
        # Get the home index
        self._homeIndex = abs(self._hash(item)) % len(self._table)
        distance = 1
        index = self._homeIndex

        # Stop searching when an empty cell is encountered
        while not self._table[index] in (HashTable.EMPTY,
                                         HashTable.DELETED):

            # Increment the index and wrap around to first 
            # position if necessary
            if self._linear:
                increment = index + 1
            else:
                # Quadratic probing
                increment = self._homeIndex + distance ** 2
                distance += 1
            index = increment % len(self._table)
            self._probeCount += 1

        # An empty cell is found, so store the item
        self._table[index] = item
        self._size += 1
        self._actualIndex = index

    def getLoadFactor(self):
        """returns the tables current load factor (#items / capacity)"""
        pass

    def getHomeIndex(self,item):
        """returns the actual index of the item most recently inserted, removed or accessed"""
        return abs(self._hash(item)) % len(self._table)

    def getActualIndex(self):
        """returns the home index of the item most recently inserted, removed or accessed """
        pass

    def getProbeCount(self):
        pass

    def get(self,item):
        """
        The get method will take the item requested as the parameter and will return the index of the item requested,
        if the item is found in the table; otherwise, the method will return -1 for item not found.
        """
        _homeIndex = self.getHomeIndex(item)
        distance = 1
        index = _homeIndex
        count = 0

        # Stop searching when the item is encountered
        while not self._table[index] == item:

            # Increment the index and wrap around to first
            # position if necessary
            #count tracks search attempts. will work for both linear and quadratic search methods
            count += 1
            if count > self.capacity: #if count surpasses the capacity of the table, the value is not in the table.
                return -1
            if self._linear:
                increment = index + 1
            else:
                # Quadratic probing
                increment = _homeIndex + distance ** 2
                distance += 1
            index = increment % len(self._table)
            self._probeCount += 1

        # The item has been found so return the index of the item requested
        return index

    def remove(self,item):
        """The remove method will take the item requested as the parameter and will return true, if the item requested
        is removed; otherwise, the method will return -1, if the item is not removed. If the method returns -1,
        then the item was not found in the table; therefore, it could not be removed.
        """
        _homeIndex = self.getHomeIndex(item)
        distance = 1
        index = _homeIndex
        count = 0

        # Stop searching when the item is encountered
        while not self._table[index] == item:

            # Increment the index and wrap around to first
            # position if necessary
            # count tracks search attempts. will work for both linear and quadratic search methods
            count += 1
            if count > self.capacity:  # if count surpasses the capacity of the table, the value is not in the table.
                return -1
            if self._linear:
                increment = index + 1
            else:
                # Quadratic probing
                increment = self._homeIndex + distance ** 2
                distance += 1
            index = increment % len(self._table)
            self._probeCount += 1

        # The item has been found so return the index of the item requested
        self._table[index] = None
        return True

    # Methods __len__(), __str__(), loadFactor(), homeIndex(),
    # actualIndex(), and probeCount() are exercises.
        
def main():
    """Uses an example data set from Chapter 19."""
    # table = HashTable(8, lambda x : x)
    # for item in (range(10, 71, 10)):
    #     table.insert(item)
    #     print("Home:", table.homeIndex(), "Probes:", table.probeCount(),
    #           "Load factor:", table.loadFactor())
    #     print(table)
    table = HashTable()
    print("inserting value: 100 to table")
    table.insert(100)
    print("inserting value: 22 to table")
    table.insert(22)
    print("using get to return value 100's index position")
    print(table.get(100))
    index = table.get(100)
    print("verifying the index position is correct...:\n",table._table[index])
    print("removing value 100. will return True when removing")
    print(table.remove(100))
    print("Now using get method will return -1.")
    print(table.get(100))
    print("verify that the index value now returns None:\n",table._table[index])


if __name__ == "__main__":
    main()
