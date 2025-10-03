"""Import time and date"""
from datetime import datetime

class Book:
    """Book class with auto-incremented ID"""
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
        self.borrowed_by = None  # Track who borrowed the book
        self.added_at = datetime.now()

    def __str__(self):
        status = "Available" if self.is_available else f"""Borrowed by Member
        {self.borrowed_by}"""
        return f"""[{self.book_id}] {self.title} by {self.author} ({self.year},
        {self.category}) - {status}"""

    def to_dict(self):
        """Serialize book data"""
        return {
            "id": self.book_id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "category": self.category,
            "available": self.is_available,
            "borrowed_by": self.borrowed_by,
            "added_at": self.added_at.isoformat(),
        }
