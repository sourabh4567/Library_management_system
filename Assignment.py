# ---------- Book Record Node (Linked List Node) ----------
class Book:
    def __init__(self, book_id, title, author, status="Available"):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.status = status  # "Available" or "Issued"
        self.next = None


# ---------- Linked List Class ----------
class BookList:
    def __init__(self):
        self.head = None

    # Insert new book
    def insert_book(self, book_id, title, author):
        new_book = Book(book_id, title, author)
        if self.head is None:
            self.head = new_book
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_book
        print("Book inserted successfully!")

    # Delete book by ID
    def delete_book(self, book_id):
        if self.head is None:
            print("No books to delete.")
            return

        if self.head.book_id == book_id:
            self.head = self.head.next
            print("Book deleted successfully!")
            return

        prev = None
        temp = self.head
        while temp and temp.book_id != book_id:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Book not found.")
        else:
            prev.next = temp.next
            print("Book deleted successfully!")

    # Search book by ID
    def search_book(self, book_id):
        temp = self.head
        while temp:
            if temp.book_id == book_id:
                return temp
            temp = temp.next
        return None

    # Display all books
    def display_books(self):
        if self.head is None:
            print("📚 No books in library.")
            return
        print("\n------ Library Book List ------")
        temp = self.head
        while temp:
            print(f"ID: {temp.book_id} | Title: {temp.title} | Author: {temp.author} | Status: {temp.status}")
            temp = temp.next
        print("--------------------------------")


# ---------- Transaction Class ----------
class Transaction:
    def __init__(self, trans_type, book_id):
        self.trans_type = trans_type  # "issue" or "return"
        self.book_id = book_id


# ---------- Stack-based Transaction Manager ----------
class TransactionManager:
    def __init__(self, book_list):
        self.book_list = book_list
        self.transaction_stack = []

    # Issue book
    def issue_book(self, book_id):
        book = self.book_list.search_book(book_id)
        if not book:
            print("Book not found.")
            return
        if book.status == "Issued":
            print("Book is already issued.")
            return
        book.status = "Issued"
        self.transaction_stack.append(Transaction("issue", book_id))
        print("Book issued successfully!")

    # Return book
    def return_book(self, book_id):
        book = self.book_list.search_book(book_id)
        if not book:
            print("Book not found.")
            return
        if book.status == "Available":
            print("Book is already available.")
            return
        book.status = "Available"
        self.transaction_stack.append(Transaction("return", book_id))
        print("Book returned successfully!")

    # Undo last transaction
    def undo_transaction(self):
        if not self.transaction_stack:
            print("No transactions to undo.")
            return

        last = self.transaction_stack.pop()
        book = self.book_list.search_book(last.book_id)
        if not book:
            return

        if last.trans_type == "issue":
            book.status = "Available"
            print("Undo: Book issue reverted!")
        elif last.trans_type == "return":
            book.status = "Issued"
            print("Undo: Book return reverted!")

    # View transaction history
    def view_transactions(self):
        if not self.transaction_stack:
            print("No transactions yet.")
            return
        print("\n------ Transaction History ------")
        for t in self.transaction_stack:
            print(f"BookID: {t.book_id} | Type: {t.trans_type}")
        print("----------------------------------")


# ---------- Main Program ----------
def main():
    book_list = BookList()
    manager = TransactionManager(book_list)

    while True:
        print("\n====== Library Book Management ======")
        print("1. Insert Book")
        print("2. Delete Book")
        print("3. Search Book")
        print("4. Display Books")
        print("5. Issue Book")
        print("6. Return Book")
        print("7. Undo Last Transaction")
        print("8. View Transactions")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_id = int(input("Enter Book ID: "))
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            book_list.insert_book(book_id, title, author)

        elif choice == "2":
            book_id = int(input("Enter Book ID to delete: "))
            book_list.delete_book(book_id)

        elif choice == "3":
            book_id = int(input("Enter Book ID to search: "))
            b = book_list.search_book(book_id)
            if b:
                print(f"Found -> Title: {b.title}, Author: {b.author}, Status: {b.status}")
            else:
                print("Book not found.")

        elif choice == "4":
            book_list.display_books()

        elif choice == "5":
            book_id = int(input("Enter Book ID to issue: "))
            manager.issue_book(book_id)

        elif choice == "6":
            book_id = int(input("Enter Book ID to return: "))
            manager.return_book(book_id)

        elif choice == "7":
            manager.undo_transaction()

        elif choice == "8":
            manager.view_transactions()

        elif choice == "9":
            print("Exiting... Thank you!")
            break

        else:
            print("Invalid choice!")


# Run program
if __name__ == "__main__":
    main()
