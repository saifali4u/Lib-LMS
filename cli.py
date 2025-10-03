"""import requirements"""
import click
from library.library import Library

lib = Library()

@click.group()
def cli():
    """📚 Library Management CLI"""


# -------------------- ADD --------------------

@cli.command()
@click.argument("title")
@click.argument("author")
@click.argument("year", type=int)
def add_book(title, author, year):
    """Add a new book"""
    book = lib.add_book(title, author, year)
    lib.save()
    click.echo(f"✅ Added book: {book}")


@cli.command()
@click.argument("name")
@click.option("--admin", is_flag=True, help="Make this member an admin")
def add_member(name, admin):
    """Add a new member"""
    member = lib.add_member(name, is_admin=admin)
    lib.save()
    click.echo(f"✅ Added member: {member}")


# -------------------- LIST --------------------

@cli.command()
def list_books():
    """List all books"""
    lib.load()
    for book in lib.books:
        borrowed_by = getattr(book, "borrowed_by", None)
        if borrowed_by:
            status = f"(Borrowed by Member {borrowed_by})"
        else:
            status = "(Available)"
        click.echo(f"{book} {status}")


@cli.command()
def list_members():
    """List all members"""
    lib.load()
    for member in lib.members.values():
        role = "Admin" if getattr(member, "is_admin", False) else "Member"
        click.echo(f"👤 {member} - {role}")


# -------------------- DELETE --------------------

@cli.command()
@click.option("--book-id", required=True, type=int, help="Book ID to delete")
def delete_book(book_id):
    """Delete a book by ID"""
    lib.load()
    book = next((b for b in lib.books if b.id == book_id), None)
    if not book:
        click.echo("❌ Book not found.")
        return
    lib.books.remove(book)
    lib.save()
    click.echo(f"🗑️ Deleted book: {book.title}")


@cli.command()
@click.option("--member-id", required=True, type=int, help="Member ID to delete")
def delete_member(member_id):
    """Delete a member by ID"""
    lib.load()
    if member_id in lib.members:
        member = lib.members[member_id]
        del lib.members[member_id]
        lib.save()
        click.echo(f"🗑️ Deleted member: {member.name}")
    else:
        click.echo("❌ Member not found.")


# -------------------- UPDATE --------------------

@cli.command()
@click.option("--book-id", required=True, type=int, help="Book ID to update")
@click.option("--title", required=False, help="New title")
@click.option("--author", required=False, help="New author")
@click.option("--year", required=False, type=int, help="New year")
def update_book(book_id, title, author, year):
    """Update book details"""
    lib.load()
    book = next((b for b in lib.books if b.id == book_id), None)
    if not book:
        click.echo("❌ Book not found.")
        return
    if title:
        book.title = title
    if author:
        book.author = author
    if year:
        book.year = year
    lib.save()
    click.echo(f"✏️ Updated book: {book}")


# -------------------- BORROW / RETURN --------------------

@cli.command()
@click.option("--book-id", required=True, type=int, help="Book ID to borrow")
@click.option("--member-id", required=True, type=int, help="Member ID borrowing the book")
def borrow_book(book_id, member_id):
    """Borrow a book for a member"""
    lib.load()
    book = next((b for b in lib.books if b.id == book_id), None)
    member = next((m for m in lib.members.values() if m.member_id == member_id), None)

    if not book or not member:
        click.echo("❌ Book or member not found.")
        return
    if getattr(book, "borrowed_by", None):
        click.echo(f"⚠️ Book '{book.title}' is already borrowed.")
        return

    book.borrowed_by = member_id
    lib.save()
    click.echo(f"📕 Book '{book.title}' borrowed by {member.name}")


@cli.command()
@click.option("--book-id", required=True, type=int, help="Book ID to return")
def return_book(book_id):
    """Return a borrowed book"""
    lib.load()
    book = next((b for b in lib.books if b.id == book_id), None)
    if not book:
        click.echo("❌ Book not found.")
        return
    if not getattr(book, "borrowed_by", None):
        click.echo(f"⚠️ Book '{book.title}' was not borrowed.")
        return

    book.borrowed_by = None
    lib.save()
    click.echo(f"📖 Book '{book.title}' has been returned.")


# -------------------- SEARCH --------------------

@cli.command()
@click.argument("query")
def search_books(query):
    """Search books by title or author"""
    lib.load()
    results = [b for b in lib.books if query.lower() in b.title.lower()
               or query.lower() in b.author.lower()]
    if not results:
        click.echo("❌ No books found.")
    else:
        for book in results:
            click.echo(f"🔍 {book}")


# -------------------- SORT --------------------

@cli.command()
@click.option("--by", type=click.Choice(["title", "author", "year"],
                                        case_sensitive=False), default="title")
def sort_books(by):
    """Sort books by title, author, or year"""
    lib.load()
    sorted_books = sorted(lib.books, key=lambda b: getattr(b, by))
    for book in sorted_books:
        click.echo(f"📚 {book}")


if __name__ == "__main__":
    cli()
