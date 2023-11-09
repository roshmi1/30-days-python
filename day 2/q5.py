# Creating a list of dictionaries representing books
books = [
    {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'year': 1925},
    {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year': 1960},
    {'title': '1984', 'author': 'George Orwell', 'year': 1949},
    # Add more books as needed
]

# Printing the titles of all the books
print("Titles of the Books:")
for book in books:
    print(book['title'])