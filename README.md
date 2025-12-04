# library-inventory-manager--abhinav-sarda-
# Library Inventory Manager

A lightweight, command-line based Library Management System built using **Object-Oriented Programming**, **JSON file handling**, and **modular Python packaging**.  
This project allows library staff to manage books, track issued/available status, and maintain records in a persistent JSON file.

---

## 🚀 Features

- Add new books with title, author, and ISBN
- Issue or return books
- Search books by title or ISBN
- View all books in the catalog
- Automatic JSON-based data persistence
- Robust exception handling
- Integrated logging for debugging and information tracking
- Modular project structure following Python package standards

---

## 📁 Project Structure

library-inventory-manager/
│
├── library_manager/
│ ├── init.py
│ ├── book.py
│ └── inventory.py
│
├── cli/
│ └── init.py
│ └── main.py
│
├── data/
│ └── books.json
│
├── README.md
├── .gitignore
└── requirements.txt


---

## 🧩 How It Works

### **1. Book Class**
- Stores book details  
- Supports issuing and returning  
- Converts object → dictionary for JSON storage  

### **2. LibraryInventory**
- Manages a list of book objects  
- Adds books, searches, displays catalog  
- Loads/saves JSON safely using try–except  

### **3. CLI Interface**
Run the program from the command line:

```bash
python cli/main.py

