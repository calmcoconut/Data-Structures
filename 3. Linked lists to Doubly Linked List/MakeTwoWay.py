# Created by Alejandro at
# 9/13/2019
"""
Define a function makeTwoWay that expects a singly linked structure as its argument. The function builds and returns
a doubly linked structure that contains the items in the singly linked structure.
(Note: The function should not alter the argument's structure.)
"""


from node import Node, TwoWayNode


def makeTwoWay(linkedList):
    """This function converts a linked list into a double linked list. Element that is fed will be made into the head
    element"""
    cur = linkedList
    #marks what element the tail will be
    tail_tracker = None

    #iterates through linked list and coverts it into a double linked list by adding previous element, tail, and head.
    #head and tail are accessible by the first element
    while cur is not None:
        TwoWayNode(cur)
        if cur.next is None:
            cur.tail = cur
            tail_tracker = cur
            break
        holder = cur
        cur = cur.next
        TwoWayNode(cur)
        cur.previous = holder
        print(cur.data)
    TwoWayNode(linkedList)
    linkedList.head = linkedList
    linkedList.previous = None
    linkedList.tail = tail_tracker


def main():
    # make driver program to test. Start by creating nodes that are in a linked structure
    a = Node(1)
    b = Node(2)
    a.next = b
    c = Node(3)
    b.next = c
    d = Node(50)
    c.next = d

    #convert to double linked list using function
    # makeTwoWay(a)
    #test by printing in both directions
    makeTwoWay(a)
    holder = a
    print("head is: ",holder.head.data)
    print("tail is: ",holder.tail)
    #traverse forward using next
    print("traversing using next")
    while holder is not None:
        print(holder.data)
        holder = holder.next

    holder = a.tail

    #traverse backward using previous
    print("\ntraversing using previous")
    while holder is not None:
        print(holder.data)
        holder = holder.previous

    print("another traversal using both methods: \n using 'next' method:",a.next.next.data,"\n using 'previous' method: ", a.next.next.previous.data)

if __name__ == '__main__':
    main()