import json
#imports Python's built-in JSON module for reading and writing JSON data
 
# ---Task 1: Read the inventory ------------------
# opens the file in read mode ("r")
# parses the JSON file and converts it into a Python list of dictionaries, stored in inventory
with open("inventory.json", "r") as f:
    inventory = json.load(f) # returns the count of books and prints it to the console
 
print(f"Total books in inventory: {len(inventory)}")
 
# ---Task 2: Update and save ------------------
# a Python dictionary representing the new book with its four fields
new_book = {
    "title": "Atomic Habits",
    "author": "James Clear",
    "price": 14.99,
    "in_stock": True
}

# adds the new book to the end of the existing list in memory 
inventory.append(new_book)

# opens the file in write mode ("w"), which overwrites the existing content 
with open("inventory.json", "w") as f:
    json.dump(inventory, f, indent=4) # writes the updated list back to the file as valid JSON, using 4-space
 
# ---Task 3: Display the updated inventory ------------------
with open("inventory.json", "r") as f:
    # reads a JSON file and returns a Python object (list or dict)
    updated_inventory = json.load(f)
 
for book in updated_inventory:
    # print the update inventory with formated price to exactly 2 decimal places
    print(f'Title: {book["title"]} | Author: {book["author"]} | Price: ${book["price"]:.2f}')
