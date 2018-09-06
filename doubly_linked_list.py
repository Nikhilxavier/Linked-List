"""
Implementation of Doubly Linked List.
"""

# Author: Nikhil Xavier <nikhilxavier@yahoo.com>
# License: BSD 3 clause


class Node:
    """Node class for Doubly Linked List."""

    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None
