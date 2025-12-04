from library_manager.inventory import LibraryInventory

def menu():
    print("\n1) Add Book  2) Issue Book  3) Return Book  4) View All  5) Search  6) Exit")
    return input("Choice: ").strip()

def main():
    inv = LibraryInventory()
    while True:
        choice = menu()
        if choice == "1":
            t = input("Title: ").strip()
            a = input("Author: ").strip()
            i = input("ISBN: ").strip()
            inv.add_book(t,a,i)
            print("Added.")
        elif choice == "2":
            isbn = input("ISBN to issue: ").strip()
            b = inv.search_by_isbn(isbn)
            if b and b.issue():
                inv.save_data()
                print("Issued.")
            else:
                print("Not found or already issued.")
        elif choice == "3":
            isbn = input("ISBN to return: ").strip()
            b = inv.search_by_isbn(isbn)
            if b and b.return_book():
                inv.save_data()
                print("Returned.")
            else:
                print("Not found or not issued.")
        elif choice == "4":
            for b in inv.display_all():
                print(b)
        elif choice == "5":
            term = input("Title or ISBN: ").strip()
            results = inv.search_by_title(term)
            if not results:
                book = inv.search_by_isbn(term)
                if book:
                    results = [book]
            if results:
                for r in results:
                    print(r)
            else:
                print("No results.")
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
