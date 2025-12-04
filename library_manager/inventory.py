import json
from pathlib import Path
from .book import Book   

class LibraryInventory:
    def __init__(self, data_file="data/books.json"):
        self.data_file = Path(data_file)
        self.data_file.parent.mkdir(parents=True, exist_ok=True)
        self.books = []
        self.load_data()

    def load_data(self):
        try:
            if not self.data_file.exists():
                self.save_data()
            with open(self.data_file, "r") as f:
                data = json.load(f)
            self.books = [Book(**b) for b in data]
        except Exception:
            self.books = []

    def save_data(self):
        with open(self.data_file, "w") as f:
            json.dump([b.to_dict() for b in self.books], f, indent=4)

    def add_book(self, title, author, isbn):
        self.books.append(Book(title, author, isbn))
        self.save_data()

    def search_by_title(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]

    def search_by_isbn(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def display_all(self):
        return self.books
