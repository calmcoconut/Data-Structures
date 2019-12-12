# Created by Alejandro at 
# 11/5/2019
"""
# Descriptions
added a rebalance method to the LinkedBST class which makes an unbalanced tree balanced. Does change the root node and
order of other nodes.

"""
from linkedbst import LinkedBST
def main():
    # Driver program to test the new rebalance method in LinkedBST class.
    # First making linked list/ vine shaped tree then will use method to create a balanced tree.
    test = LinkedBST()
    test.add(30)
    for i in range(29):
        test.add(i)
    print(test)

    # now rebalance tree to be a balanced BST... Root and order of nodes will change:
    test.rebalance()
    print(test)

    #example 2
    test2 = LinkedBST()
    test2.add("A")
    test2.add("F")
    test2.add("G")
    test2.add("J")
    test2.add("P")
    test2.add("R")
    test2.add("S")
    test2.add("T")
    test2.add("W")
    test2.add("Z")
    print(test2)
    test2.rebalance()
    print(test2)
if __name__ == "__main__":
    main()
