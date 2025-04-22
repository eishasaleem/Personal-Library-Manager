import os
import json

# File to save/load the library
FILE_NAME = "library.txt"

def load_library():
    """Load the library from a file."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return []

def save_library(library):
    """Save the library to a file."""
    with open(FILE_NAME, 'w') as file:
        json.dump(library, file)

def add_book(library):
    """Add a new book to the library."""
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    try:
        year = int(input("Enter the publication year: "))
    except ValueError:
        print("Invalid year. Book not added.")
        return
    genre = input("Enter the genre: ")
    read_input = input("Have you read this book? (yes/no): ").strip().lower()
    read = read_input == 'yes'
    
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }
    library.append(book)
    print("Book added successfully!")

def remove_book(library):
    """Remove a book by title."""
    title = input("Enter the title of the book to remove: ").strip()
    original_count = len(library)
    library[:] = [book for book in library if book['title'].lower() != title.lower()]
    
    if len(library) < original_count:
        print("Book removed successfully!")
    else:
        print("Book not found.")

def search_books(library):
    """Search for books by title or author."""
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ").strip()
    query = input("Enter the search term: ").strip().lower()

    if choice == '1':
        results = [book for book in library if query in book['title'].lower()]
    elif choice == '2':
        results = [book for book in library if query in book['author'].lower()]
    else:
        print("Invalid choice.")
        return
    
    if results:
        print("Matching Books:")
        for i, book in enumerate(results, start=1):
            print_book(i, book)
    else:
        print("No matching books found.")

def display_books(library):
    """Display all books in the library."""
    if not library:
        print("Your library is empty.")
    else:
        print("Your Library:")
        for i, book in enumerate(library, start=1):
            print_book(i, book)

def display_statistics(library):
    """Display total books and percentage read."""
    total = len(library)
    read_count = sum(1 for book in library if book['read'])
    percent_read = (read_count / total * 100) if total > 0 else 0
    print(f"Total books: {total}")
    print(f"Percentage read: {percent_read:.1f}%")

def print_book(index, book):
    """Print a single book's details."""
    status = "Read" if book['read'] else "Unread"
    print(f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

def main():
    library = load_library()
    while True:
        print("\nMenu")
        print("Welcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_books(library)
        elif choice == '4':
            display_books(library)
        elif choice == '5':
            display_statistics(library)
        elif choice == '6':
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
