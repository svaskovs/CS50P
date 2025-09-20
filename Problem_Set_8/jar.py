class Jar:
    def __init__(self, capacity, size):
        if capacity < 0:
            raise ValueError
        self.capacity = capacity
        self.size = size

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if (self.capacity - self.size) >= n and n > 0:
            self.size += n
        else: return ValueError

    def withdraw(self, n):
        if self.size >= n and n > 0:
            self.size -= n
        else: return ValueError
    
    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size