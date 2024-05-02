class Image:
    def __init__(self, id, name, user, size, format):
        self.id = id
        self.name = name
        self._size = size
        self._format = format

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, newSize):
        self._size = newSize

    @property
    def format(self):
        return self._format

    @format.setter
    def format(self, newFormat):
        self._format = newFormat
