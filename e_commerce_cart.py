def calculate_total(cart):
    if not cart:
        return "Cart is empty."
    total_price = sum(cart.values())
    total_items = len(cart)
    if total_items > 5:
        total_price *= 0.9
    return f" Total Price: {int(total_price)}"

cart = {}
print("Enter items (type 'done' to finish):")
while True:
    item = input("Item: ")
    if item.lower() == 'done':
        break
    price = float(input("Price: "))
    cart[item] = price

print(calculate_total(cart))
