def add_book(catalog, book_id, title, author, year):
    catalog[book_id] = (title, author, year)


def borrow_book(catalog, borrowed_books, book_id):
    if book_id not in catalog:
        print(f"Book ID {book_id} does not exist in the catalog.")
    elif book_id in borrowed_books:
        print(f"Book ID {book_id} is already borrowed.")
    else:
        borrowed_books.append(book_id)
        title, author, year = catalog[book_id]
        print(f"Borrowed: {title} by {author} ({year})")


def return_book(borrowed_books, book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print(f"Returned book ID {book_id}.")
    else:
        print(f"Book ID {book_id} was not borrowed.")


def register_member(members, member_id):
    members.add(member_id)


def show_available(catalog, borrowed_books):
    print("\nAvailable Books:")
    borrowed_set = set(borrowed_books)

    found_available = False
    for book_id, details in catalog.items():
        if book_id not in borrowed_set:
            title, author, year = details
            print(f"{book_id}: {title} by {author} ({year})")
            found_available = True

    if not found_available:
        print("No books are currently available.")


def main():
    catalog = {}
    borrowed_books = []
    members = set()

    add_book(catalog, 101, "Python Basics", "R. Sharma", 2022)
    add_book(catalog, 102, "Clean Code", "Robert C. Martin", 2008)
    add_book(catalog, 103, "Data Structures", "N. Patel", 2021)
    add_book(catalog, 104, "Automate the Boring Stuff", "Al Sweigart", 2019)

    register_member(members, "M001")
    register_member(members, "M002")
    register_member(members, "M003")
    register_member(members, "M002")

    print("Registered Members:", members)

    borrow_book(catalog, borrowed_books, 101)
    borrow_book(catalog, borrowed_books, 103)

    return_book(borrowed_books, 101)

    print("Currently Borrowed Book IDs:", borrowed_books)
    show_available(catalog, borrowed_books)


if __name__ == "__main__":
    main()
