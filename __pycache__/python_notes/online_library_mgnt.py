
print("------ ONLINE LIBRARY MANAGEMENT SYSTEM ------")

# List of available books
books = ["Python", "Java", "C++"]
print("Available Books:")
print(books)

# String operation - uppercase
uppercase_books = [book.upper() for book in books]
print("\nUppercase Book Names:")
print(uppercase_books)

# Tuple - Book categories
categories = ("Programming", "Database", "Networking")
print("\nBook Categories:")
for category in categories:
    print(category)

# Set - Unique genres
genres = set(books)
print("\nUnique Genres:")
print(genres)

# Dictionary - Book details
book_details = {
    101: {"title": "Python", "author": "Alex"}
}

print("\nBook Details:")
for book_id, details in book_details.items():
    print(book_id, "->", details)

# Dictionary with two books
library = {
    101: {"title": "Python"},
    102: {"title": "Java"}
}

print("\nDictionary Keys:")
print(library.keys())

print("\nDictionary Values:")
print(library.values())

# None
book_issued = None

print("\nBook Not Issued:")
print(book_issued)

print("Type of None:")
print(type(book_issued))

# Hash value
book_hash = hash("Python")

print("\nHash Value:")
print(book_hash)