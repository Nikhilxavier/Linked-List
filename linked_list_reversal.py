"""
Implementation of n to last node finder.
"""

# Author: Nikhil Xavier <nikhilxavier@yahoo.com>
# License: BSD 3 clause


class Node:
    """Node class for Singly Linked List."""

    def __init__(self, value):
        self.value = value
        self.next_node = None


def n2last_node(n, head):
    """Find n to last node in Linked List.

    Returns n from last node.
    """
    first_node = head
    second_node = head

    for _ in range(n):
        if not second_node:
            raise LookupError("Error: Insufficient nodes in linked list")
        second_node = second_node.next_node

    while second_node.next_node:
        second_node = second_node.next_node
        first_node = first_node.next_node

    return first_node
