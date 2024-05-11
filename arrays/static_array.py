class StaticArr:
    def __init__(self, allocation_size=8):
        self.allocation_size = allocation_size
        self._placeholder = "-!@!-"
        self._array = [self._placeholder] * self.allocated_size
        self._end_point = 0
