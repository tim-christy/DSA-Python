class StaticArr:
    def __init__(self, allocation_size=8):
        self.allocation_size = allocation_size
        self._placeholder = "-!@!-"
        self._array = [self._placeholder] * self.allocated_size
        self._end_point = 0

    def size(self):
        """Returns size of the array, i.e. number of elements in the array"""
        return self._end_point + 1

    def append(self, val):
        """Appends val to the array if space is available. Otherwise errors"""
        if self._end_point != self.allocation_size - 1:
            self._array[self._end_point] = val
            self._end_point += 1
        else:
            raise IndexError(
                "Array is full and cannot be added to. Use insert()"
            )

    def insert(self, index, val):
        """
        Inserts val at the index position.
        If the array is full, the value at the index will be overwritten.
        If the array is not full, all values will be shifted down an index.
        """
        # Boundary check
        if index >= self.allocation_size or index < 0:
            raise IndexError("Insertion index is out of bounds")

        # If the array is full - ie pointer is at the end of array
        elif self._end_point == self.allocation_size - 1:
            # Overwrite the value at the given index
            self._array[index] = val
            self._index

        # Else there's still room for everyone in the array
        else:
            # Starting from the end value and going down to just before index
            for i in range(self._end_point, index + 1, -1):
                # Shift everything over
                self._array[i + 1] = self._array[i]
            # Insert the value at the desired index
            self._array[index] = val

            # Increment our end pointer
            self._end_point += 1
