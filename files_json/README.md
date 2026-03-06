# Working with Files and JSON in Python

## Overview
This program manages a bookstore inventory stored in a JSON file called inventory.json. It reads the current inventory, adds a new book, saves the updated data back to the file, and finally displays all books in a formatted output.

** Starter File — inventory.json **
The initial contents of inventory.json are:
```json
[
  {"title": "The Alchemist", "author": "Paulo Coelho", "price": 12.99, "in_stock": true},
  {"title": "1984", "author": "George Orwell", "price": 9.99, "in_stock": true}
]
```

The new book to be added is defined as:
```json
new_book = {"title": "Atomic Habits", "author": "James Clear", "price": 14.99, "in_stock": True}
```

## Task 1 — Read the Inventory

```python
with open("inventory.json", "r") as f:
    inventory = json.load(f)
 
print(f"Total books in inventory: {len(inventory)}")
```

** Explanation **

* import json — imports Python's built-in JSON module for reading and writing JSON data.
* open("inventory.json", "r") — opens the file in read mode ("r").
* The with block ensures the file is automatically closed after use, even if an error occurs. This is the recommended best practice for file handling.
* json.load(f) — parses the JSON file and converts it into a Python list of dictionaries, stored in inventory.
* len(inventory) — returns the count of books and prints it to the console.


** Expected output: **

```terminal
Total books in inventory: 2
```


## Task 2 — Update and Save

```python
new_book = {
    "title": "Atomic Habits",
    "author": "James Clear",
    "price": 14.99,
    "in_stock": True
}

inventory.append(new_book)
 
with open("inventory.json", "w") as f:
    json.dump(inventory, f, indent=4)
``` 

** Explanation **

* new_book — a Python dictionary representing the new book with its four fields.
* inventory.append(new_book) — adds the new book to the end of the existing list in memory.
* open("inventory.json", "w") — opens the file in write mode ("w"), which overwrites the existing content.
* json.dump(inventory, f, indent=4) — writes the updated Python list back to the file as valid JSON, using 4-space indentation for readability.
* Again, the with block ensures the file is properly closed after writing.


## Task 3 — Display the Updated Inventory

```python
with open("inventory.json", "r") as f:
    updated_inventory = json.load(f)
 
for book in updated_inventory:
    print(f'Title: {book["title"]} | Author: {book["author"]} | Price: ${book["price"]:.2f}')
```

** Explanation **

* The file is opened and read again to confirm the data was saved correctly (re-reading from disk rather than just using the in-memory list).
* A for loop iterates over each book dictionary in the list.
* An f-string formats each book's details into the required output format.
* {book["price"]:.2f} — formats the price to exactly 2 decimal places (e.g., 9.99 → $9.99).

** Expected output: **

```terminal
Title: The Alchemist | Author: Paulo Coelho | Price: $12.99
Title: 1984 | Author: George Orwell | Price: $9.99
Title: Atomic Habits | Author: James Clear | Price: $14.99
```

