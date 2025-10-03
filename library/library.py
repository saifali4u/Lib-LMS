"""Import following requirements"""
import json
import os
from .book import Book
from .member import Member
from .admin import Admin
from .utils import log_action
from .iterator import LibraryIterator

class Library:
    """Create Library class"""
    def __init__(self, filename="library.json"):
        self.books : list = []
        self.members = {}
        self.filename = filename
        if os.path.exists(self.filename):
            self.load()

    @log_action
    def add_book(self, title, author, year, category="General"):
        """MAKE A add_book function"""
        book = Book(title, author, year, category)
        self.books.append(book)
        return book

    @log_action
    def add_member(self, name, is_admin=False):
        """MAKE A add_member function"""
        member = Admin(name) if is_admin else Member(name)
        self.members[member.member_id] = member
        return member

    def list_books(self):
        """MAKE A list_book function"""
        return LibraryIterator(self.books)

    def save(self):
        """MAKE A save function"""
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump({
                "books": [b.to_dict() for b in self.books],
                "members": {mid: m.to_dict() for mid, m in self.members.items()}
            }, f, indent=4)

    def load(self):
        """MAKE A load function"""
        with open(self.filename, encoding="utf-8") as f:
            data = json.load(f)
            for b in data["books"]:
                self.books.append(Book(b["title"], b["author"], b["year"], b["category"]))
            for mid, m in data["members"].items():
                member = Admin(m["name"]) if m["is_admin"] else Member(m["name"])
                self.members[int(mid)] = member
