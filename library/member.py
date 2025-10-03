"""MAKE A class"""
class Member:
    """MAKE A class with auto increment"""
    _id_counter = 1

    def __init__(self, name):
        if not name.strip():
            raise ValueError("Name cannot be empty")
        self.member_id = Member._id_counter
        Member._id_counter += 1
        self.name = name
        self.borrowed_books = {}

    def __str__(self):
        return f"Member {self.member_id}: {self.name} (Borrowed: {len(self.borrowed_books)})"

    def to_dict(self):
        """MAKE A function"""
        return {
            "id": self.member_id,
            "name": self.name,
            "borrowed": self.borrowed_books,
            "is_admin": False,
        }
