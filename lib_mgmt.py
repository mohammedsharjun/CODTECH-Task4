import datetime

# Base class to represent a library item
class LibraryItem:
    def __init__(self, item_id, title, author, category):
        self.item_id = item_id
        self.title = title
        self.author = author
        self.category = category
        self.is_checked_out = False

# Derived class for books
class Book(LibraryItem):
    def __init__(self, item_id, title, author, genre):
        super().__init__(item_id, title, author, 'Book')
        self.genre = genre

# Derived class for magazines
class Magazine(LibraryItem):
    def __init__(self, item_id, title, author, issue):
        super().__init__(item_id, title, author, 'Magazine')
        self.issue = issue

# Derived class for DVDs
class DVD(LibraryItem):
    def __init__(self, item_id, title, director, duration):
        super().__init__(item_id, title, director, 'DVD')
        self.duration = duration

# Class to manage library items
class Library:
    def __init__(self):
        self.items = []
        self.issued_items = []
        self.next_item_id = 1001
        self.fine_rate = 5  # Fine rate per day

    def add_item(self, item):
        self.items.append(item)
        print(f"Item added: {item.title} ({item.category})")

    def generate_item_id(self):
        item_id = self.next_item_id
        self.next_item_id += 1
        return item_id

    def check_out_item(self, item_id, member_id):
        item = self.find_item(item_id)
        if item and not item.is_checked_out:
            item.is_checked_out = True
            issue_date = datetime.datetime.now()
            self.issued_items.append((item, member_id, issue_date))
            print(f"{item.title} checked out by Member ID: {member_id} on {issue_date.strftime('%Y-%m-%d')}")
        else:
            print("Item not available for checkout.")

    def return_item(self, item_id, member_id):
        for record in self.issued_items:
            item, mid, issue_date = record
            if item.item_id == item_id and mid == member_id:
                return_date = datetime.datetime.now()
                duration = (return_date - issue_date).days
                fine = max(0, duration - 14) * self.fine_rate  # Assuming a 14-day loan period
                if fine > 0:
                    print(f"Overdue! Fine is ${fine}.")
                else:
                    print("Item returned on time. No fine.")
                item.is_checked_out = False
                self.issued_items.remove(record)
                return
        print("Item not found in issued records.")

    def find_item(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                return item
        print("Item not found.")
        return None

    def search_items(self, search_term):
        results = [item for item in self.items if search_term.lower() in item.title.lower() or search_term.lower() in item.author.lower() or search_term.lower() in item.category.lower()]
        if results:
            for item in results:
                print(f"ID: {item.item_id}, Title: {item.title}, Author: {item.author}, Category: {item.category}, Checked Out: {item.is_checked_out}")
        else:
            print("No items found matching search criteria.")

    def display_items(self):
        for item in self.items:
            status = 'Checked Out' if item.is_checked_out else 'Available'
            print(f"ID: {item.item_id}, Title: {item.title}, Author: {item.author}, Category: {item.category}, Status: {status}")
        if not self.items:
            print("No items in library.")

# Main function to run the library management system
def main():
    library = Library()

    while True:
        print("\nLibrary Management System\n")
        print("1. Add Item")
        print("2. Check Out Item")
        print("3. Return Item")
        print("4. Search Items")
        print("5. Display All Items")
        print("6. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            item_type = input("Enter item type (Book/Magazine/DVD): ").lower()
            title = input("Enter title: ")
            author = input("Enter author: ")
            item_id = library.generate_item_id()

            if item_type == 'book':
                genre = input("Enter genre: ")
                item = Book(item_id, title, author, genre)
            elif item_type == 'magazine':
                issue = input("Enter issue: ")
                item = Magazine(item_id, title, author, issue)
            elif item_type == 'dvd':
                director = input("Enter director: ")
                duration = input("Enter duration: ")
                item = DVD(item_id, title, director, duration)
            else:
                print("Invalid item type!")
                continue

            library.add_item(item)

        elif choice == '2':
            item_id = int(input("Enter item ID to check out: "))
            member_id = input("Enter member ID: ")
            library.check_out_item(item_id, member_id)

        elif choice == '3':
            item_id = int(input("Enter item ID to return: "))
            member_id = input("Enter member ID: ")
            library.return_item(item_id, member_id)

        elif choice == '4':
            search_term = input("Enter search term: ")
            library.search_items(search_term)

        elif choice == '5':
            library.display_items()

        elif choice == '6':
            print("Exiting system.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
