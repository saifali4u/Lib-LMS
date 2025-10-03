"""Import .member form Member Class"""
from .member import Member
class Admin(Member):
    """Create Admin class and then inherit"""
    def __str__(self):
        return f"Admin {self.member_id}: {self.name} (Borrowed: {len(self.borrowed_books)})"

    def to_dict(self):
        data = super().to_dict()
        data["is_admin"] = True
        return data
