"""MAKE A class"""
class LibraryIterator:
    """Create a class"""
    def __init__(self, books):
        self._books = books
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._books):
            book = self._books[self._index]
            self._index += 1
            return book
        raise StopIteration
