"""
File: linkedlist.py
Author: Ken Lambert

Modified by Alejandro Diaz 10.30.2019

"""

from node import TwoWayNode
from abstractlist import AbstractList

class LinkedList(AbstractList):
    """A link-based list implementation."""

    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        # Uses a circular linked structure with a dummy header node
        self._head = TwoWayNode()
        self._head.previous = self._head.next = self._head
        AbstractList.__init__(self, sourceCollection)

    # Helper method returns node at position i
    def _getNode(self, i):
        """Helper method: returns a pointer to the node at position i."""
        if i == len(self):
            return self._head
        elif i == len(self) - 1:
            return self._head.previous
        probe = self._head.next
        while i > 0:
            probe = probe.next
            i -= 1
        return probe

    #Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = self._head.next
        while cursor != self._head:
            yield cursor.data
            cursor = cursor.next

    def __getitem__(self, i):
        """Precondition: 0 <= i < len(self)
        Returns the item at position i.
        Raises: IndexError."""
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        return self._getNode(i).data

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._head = TwoWayNode()
        self._head.previous = self._head.next = self._head
        
    def __setitem__(self, i, item):
        """Precondition: 0 <= i < len(self)
        Replaces the item at position i.
        Raises: IndexError."""
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        self._getNode(i).data = item

    def insert(self, i, item):
        """Inserts the item at position i."""
        if i < 0: i = 0
        elif i > len(self): i = len(self)
        theNode = self._getNode(i)
        newNode = TwoWayNode(item, theNode.previous, theNode)
        theNode.previous.next = newNode
        theNode.previous = newNode
        self._size += 1
        self.incModCount()

    def pop(self, i = None):
        """Precondition: 0 <= i < len(self).
        Removes and returns the item at position i.
        If i is None, i is given a default of len(self) - 1.
        Raises: IndexError."""
        if i == None: i = len(self) - 1
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        theNode = self._getNode(i)
        item = theNode.data
        theNode.previous.next = theNode.next
        theNode.next.previous = theNode.previous
        self._size -= 1
        self.incModCount()
        return item

    def listIterator(self):
        """Returns a list iterator."""
        return LinkedList.ListIterator(self)

    class ListIterator(object): #TODO alter the cursor to track nodes within the backing sore's linked structure...
        # The navigational methods adjust the cursor setting it to next node or the previous node
        """Represents the list iterator for linked list.
        Preconditions:
        - Cannot run the next or previous operations if the hasNext or hasPrevious operations return False.
        - Cannot run a consecutive mutator method. a next or previous must be ran beforehand
        - Cannot run mutations on the list itself, with the list's mutator methods, while using a list iterator on
            the list.
        """

        def __init__(self, backingStore):
            self._backingStore = backingStore
            self._modCount = backingStore.getModCount()
            self.first()

        def first(self):
            """Returns the cursor to the beginning of the backing store."""
            self._cursor = self._backingStore._head.next
            self._lastItemPos = self._backingStore._head
            self._lastIndex = -1
            # self._firstIndex = 0

        def hasNext(self): # TODO alter for linked list application. Done.
            """Returns True if the iterator has a next item or False otherwise."""
            if self._lastItemPos.next.data is not None and self._cursor != self._backingStore._head:
                return True
            else:
                return False
            # return self._cursor < len(self._backingStore)

        def next(self): # TODO alter for linked list application. Done.
            """Preconditions: hasNext returns True
            The list has not been modified except by this iterator's mutators.
            Returns the current item and advances the cursor to the next item.
            Postcondition: lastItemPos is now defined.
            Raises: ValueError if no next item.
            AttributeError if illegal mutation of backing store."""
            if not self.hasNext():
                raise ValueError("No next item in list iterator")
            if self._modCount != self._backingStore.getModCount():
                raise AttributeError("Illegal modification of backing store")
            self._lastItemPos = self._cursor
            self._cursor = self._cursor.next
            self._lastIndex += 1
            # self._firstIndex += 1
            return self._lastItemPos.data

        def last(self): # TODO alter for linked list application. Done
            """Moves the cursor to the end of the backing store."""
            self._cursor = self._backingStore._head
            self._lastItemPos = self._backingStore._head.previous
            self._lastIndex = self._backingStore._size


        def hasPrevious(self): # TODO alter for linked list application. Done
            """Returns True if the iterator has a previous item or False otherwise."""
            if self._cursor.previous.data is not None:
                return True
            else:
                return False
            # return self._cursor < len(self._backingStore)

        def previous(self): # TODO alter for linked list application. Done
            """Preconditions: hasPrevious returns True
            The list has not been modified except by this iterator's mutators.
            Returns the current item and moves the cursor to the previous item.
            Postcondition: lastItemPos is now defined.
            Raises: ValueError if no next item.
            AttributeError if illegal mutation of backing store."""
            if not self.hasPrevious():
                raise ValueError("No previous item in list iterator")
            if self._modCount != self._backingStore.getModCount():
                raise AttributeError("Illegal modification of backing store")
            self._cursor = self._cursor.previous
            self._lastItemPos = self._cursor.previous
            self._lastIndex -= 1
            # self._firstIndex -= 1
            return self._cursor.data

        def replace(self, item): # TODO alter for linked list application. DONE.
            """Preconditions: the current position is defined.
            The list has not been modified except by this iterator's mutators.
            Replaces the items at the current position with item.
            Raises: AttibuteError if position is not defined.
            AttributeError if illegal mutation of backing store."""
            if self._lastItemPos == self._backingStore._head:
                raise AttributeError("The current position is undefined.")
            if self._modCount != self._backingStore.getModCount():
                raise AttributeError("List has been modified illegally.")
            self._lastItemPos.data = item
            self._lastItemPos = self._backingStore._head
            # self._backingStore[self._lastItemPos] = item
            # self._lastItemPos = -1

        def insert(self, item): #TODO alter for linked list application. Done.
            """Preconditions:
            The list has not been modified except by this iterator's mutators.
            Adds item to the end if the current position is undefined, or
            inserts it at that position.
            Raises: AttributeError if illegal mutation of backing store."""
            if self._modCount != self._backingStore.getModCount():
                raise AttributeError("List has been modified illegally.")
            if self._lastItemPos == self._backingStore._head:
                self._backingStore.add(item)
            else:
                self._backingStore.insert(self._lastIndex, item)
                self._lastItemPos = self._backingStore._head
            self._modCount += 1


        def remove(self): #TODO alter for linked list application.
            """Preconditions: the current position is defined.
            The list has not been modified except by this iterator's mutators.
            Pops the item at the current position.
            Raises: AttibuteError if position is not defined.
            AttributeError if illegal mutation of backing store."""
            if self._lastItemPos == self._backingStore._head and self._lastIndex == -1:
                raise AttributeError("The current position is undefined.")
            if self._lastIndex < 0:
                self._lastIndex = 0
            if self._modCount != self._backingStore.getModCount():
                raise AttributeError("List has been modified illegally.")
            else:
                if self._lastIndex == -1:
                    self._lastIndex = 0
                item = self._backingStore.pop(self._lastIndex)
            # If the item removed was obtained via next, move cursor back
            # if self._lastItemPos.previous is self._backingStore._head:
            #     self._lastIndex -= 1
            if self._lastItemPos.next.data is not None:
                self._lastIndex -= 1
            self._modCount += 1
            self._lastItemPos = self._backingStore._head

