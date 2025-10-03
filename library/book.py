"""Import datetime"""
from datetime import datetime

class Book:
    """MAKE A Book class with auto increment"""
    _id_counter = 1

    def __init__(self, title, author, year, category="General"):
        if not title or not author:
            raise ValueError("Title and author cannot be empty")
        if not str(year).isdigit() or len(str(year)) != 4:
            raise ValueError("Year must be a valid 4-digit number")

        self.book_id = Book._id_counter
        Book._id_counter += 1
        self.title = title
        self.author = author
        self.year = int(year)
        self.category = category
        self.is_available = True
        self.added_at = datetime.now()

    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"
        return f"""[{self.book_id}] {self.title} by {self.author} ({self.year},
        {self.category}) - {status}"""

    def to_dict(self):
        """MAKE A add_book function"""
        return {
            "id": self.book_id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "category": self.category,
            "available": self.is_available,
            "added_at": self.added_at.isoformat(),
        }
