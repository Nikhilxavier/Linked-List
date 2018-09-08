"""
Implementation of Linked List reversal.
"""

# Author: Nikhil Xavier <nikhilxavier@yahoo.com>
# License: BSD 3 clause


class Node:
    """Node class for Singly Linked List."""

    def __init__(self, value):
        self.value = value
        self.next_node = None


def reverse_linked_list(head):
    """Reverse linked list.

    Returns reversed linked list head.
    """
    current_node = head
    previous_node = None
    next_node = None

    while current_node:
        next_node = current_node.next_node
        current_node.next_node = previous_node
        previous_node = current_node
        current_node = next_node

    return previous_node
