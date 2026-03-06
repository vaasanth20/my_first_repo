import json
 
# ---Task 1: Read the inventory ------------------
with open("inventory.json", "r") as f:
    inventory = json.load(f)
 
print(f"Total books in inventory: {len(inventory)}")
 
# ---Task 2: Update and save ------------------
new_book = {
    "title": "Atomic Habits",
    "author": "James Clear",
    "price": 14.99,
    "in_stock": True
}
 
inventory.append(new_book)
 
with open("inventory.json", "w") as f:
    json.dump(inventory, f, indent=4)
 
# ---Task 3: Display the updated inventory ------------------
with open("inventory.json", "r") as f:
    updated_inventory = json.load(f)
 
for book in updated_inventory:
    print(f'Title: {book["title"]} | Author: {book["author"]} | Price: ${book["price"]:.2f}')
