class Image:
    def __init__(self, id, name, size, format, user):
        self.id = id
        self.name = name
        self._size = size
        self._format = format
        self._user = user

    @property
    def user(self):
        return self._user

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

