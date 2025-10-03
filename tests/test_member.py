"""Import the requirements"""
from library.member import Member

def test_member_creation():
    """make a fucntion"""
    m = Member("Alice")
    assert m.name == "Alice"
    assert m.member_id >= 1
