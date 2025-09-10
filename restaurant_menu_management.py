def add_item(menu, item):
    menu.append(item) if item not in menu else None
def remove_item(menu, item):
    menu.remove(item) if item in menu else print(f"{item} does not exist in the menu.")
def check_item(menu, item):
    return f"\"{item} is available\"" if item in menu else f"\"{item} is not available\""
menu = input("Enter initial menu items (comma separated): ").split(",")
add_item(menu, input("Enter item to add: "))
remove_item(menu, input("Enter item to remove: "))
availability = check_item(menu, input("Enter item to check: "))
print("\nUpdated menu:", menu)
print("Availability:", availability)
