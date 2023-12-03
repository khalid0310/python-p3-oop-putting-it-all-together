#!/usr/bin/env python3
# lib/shoe.py

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = None  # Use a private variable to store size
        self.size = size  # Use the property setter to perform validation
        self.condition = "New"  # Default condition

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
