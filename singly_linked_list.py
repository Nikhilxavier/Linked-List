"""
Implementation of Singly Linked List.
"""

# Author: Nikhil Xavier <nikhilxavier@yahoo.com>
# License: BSD 3 clause


class Node:
    """Node class for Singly Linked List."""

    def __init__(self, value):
        self.value = value
        self.next_node = None
