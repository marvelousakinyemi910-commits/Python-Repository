

import random
books = [
            "7 habits of highly effective people",
            "The Richest man in Babylon",
            "Men are from Mars, Women are from Venus",
            "Atomic Habit",
            "Nearly all the men in Lagos are mad",        
            "Last days at Forcados high school",
            "Independence"
    ]


def book_suggestion_menu():
   
        print("""
        Welcome to the Book Suggestion System!
        1.Get Suggestions
        2. Add Book
        3. Remove Book
        4. Update book
        5. Show books
        6. Exit
        """)
        
        
   




def get_suggestion():
    while True:
        book = random.choice(books) 
        page = random.randint(1, 100)
        print("\nBook for Day:")
        print("Book Title:",book)
        print("page:",page)
        choice = input("Do you want another suggestion? (yes/no): ")
        if choice.lower()== "no":
            break
        
def add_book(): 
    book = input("Enter book title to add: ") 
    if book in books:
        print("Book already exist")   
    else:
        books.append(book)
        print("Book successfully added")

def remove_book():
    book = input("Enter book title to remove: ")
    if book in books:
        books.remove(book)
        print("Book successfully removed")
    else:
        print("Book not found")

def update_book():
    old_book = input("Enter book title to update: ")
    if old_book in books:
        new_book = input("Enter new book title: ")
        index = books.index(old_book)
        books[index] = new_book
        print("Book successfully updated")
    else:
        print(" Book not found")
def show_books():
    print("\nAvailable books:")  
    for book in  books:
        print("-",book)     


while True:
    book_suggestion_menu()
    option = input("Enter operation: ")
    
    if option == "1":
        get_suggestion()
    elif option == "2":
        add_book()
    elif option == "3":
        remove_book()
    elif option  == "4":
        update_book()
    elif option == "5":
        show_books()
    elif option == "6":
        print("Goodbye!g")
        break
    else:
        print("Invalid option!")







