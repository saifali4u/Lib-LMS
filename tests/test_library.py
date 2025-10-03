"""import the requirements"""
from library.library import Library

def test_add_book_and_member(tmp_path):
    """make a fucntion for testing of membere and book"""
    lib = Library(filename=tmp_path / "data.json")
    b = lib.add_book("Python 101", "Guido", 2020)
    m = lib.add_member("Alice")
    lib.save()
    assert b.title == "Python 101"
    assert m.name == "Alice"
