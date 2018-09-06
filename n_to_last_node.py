"""
Implementation of cycle check in Singly Linked List.
"""

# Author: Nikhil Xavier <nikhilxavier@yahoo.com>
# License: BSD 3 clause


class Node:
    """Node class for Singly Linked List."""

    def __init__(self, value):
        self.value = value
        self.next_node = None


def cycle_checker(node):
    """Check if the Singly Linked List is cyclic.

    Returns boolean value based on the result
    """
    marker_1 = node
    marker_2 = node
    flag = False

    while marker_2 != None and marker_2.next_node != None:
        marker_1 = marker_1.next_node
        marker_2 = marker_2.next_node.next_node
        if marker_1 == marker_2:
            return True
    return False
