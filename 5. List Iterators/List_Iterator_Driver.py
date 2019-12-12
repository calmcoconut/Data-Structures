# Created by Alejandro at 
# 10/30/2019
"""
# Descriptions
driver program to test Linked list, list iterator methods

"""
from linkedlist import LinkedList

def main():
    lyst = LinkedList()
    lyst.add(5)
    lyst.add(10)
    lyst.add(15)
    listIterator = lyst.listIterator()

    print("Removing all items (reverse): Expect []: ", end = "")
    listIterator.last()
    while listIterator.hasPrevious():
        listIterator.previous()
        listIterator.remove()
    print(lyst)
    print("Length:", len(lyst))

    lyst = LinkedList()
    lyst.add(5)
    lyst.add(10)
    lyst.add(15)
    lyst.add(25)
    listIterator = lyst.listIterator()

    print("Removing all items (forward): Expect []: ", end = "")
    listIterator.first()
    while listIterator.hasNext():
        listIterator.next()
        listIterator.remove()
    print(lyst)
    print("Length:", len(lyst))
if __name__ == '__main__':
    main()