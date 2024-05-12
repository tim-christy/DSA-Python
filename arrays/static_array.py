class StaticArr:
    def __init__(self, allocation_size=8):
        self.allocation_size = allocation_size
        self._placeholder = "-!@!-"
        self._array = [self._placeholder] * self.allocation_size
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

    def clear(self):
        """Remove all elements from the array"""
        for i in range(self.allocation_size):
            self._array[i] = self._placeholder

    def copy(self):
        """Return a copy of the array"""
        import copy

        return copy.deepcopy(self._array)

    def count(self, val):
        """Return the number of occurences of val"""
        count = 0
        for el in self._array[: self._end_point]:
            if el == val:
                count += 1
        return count

    def extend(self, it):
        """
        Extend a list with staticArr. Will only fill up to the available space
        """
        for i in it:
            if self._end_point == self._length - 1:
                return
            else:
                self.append(i)

    def index(self, val, start_index=0, end_index=None):
        """
        Return the index of the first found value within the provided start and
        end indices. Returns -1 if not found
        """
        if end_index is None:
            index_arr = self._array[start_index:].copy()
        else:
            index_arr = self._array[start_index:end_index].copy()

        for i in range(len(index_arr)):
            if index_arr[i] == val:
                return i
        return -1

    def pop(self, index=-1):
        """
        Remove the value at the index or the last value in the array if no
        index provided.
        """
        if index >= self.allocation_size:
            raise IndexError("Index out of bounds")
        return_val = self._array[index]

        # Now overwrite everything and shift down
        for i in range(index, self._end_point):
            self._array[i] = self._array[i + 1]
        self._end_point -= 1
        self._array[self._end_point + 1:] = self._placeholder
        return return_val

    def get(self, index):
        """Return the value at an index"""
        return self._array[index]

    def reverse(self):
        """Reverse the list"""
        # This is probably shortcutting and I'm missing out on an algorithm
        return self._array[::-1]

    def sort():
        """Sort the list"""
        pass
