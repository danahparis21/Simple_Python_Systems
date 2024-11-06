print("Welcome! Please place your order.")
coffee_menu = [
    {"flavor": "Mocha", "price": 105},
    {"flavor": "Americano", "price": 95},
    {"flavor": "Brewed", "price": 100},
    {"flavor": "Hazelnut", "price": 125},
    {"flavor": "Vanilla", "price": 135},
    {"flavor": "Caramel", "price": 150},
]

trans_type = {
    'take-out': 0.0002, 
    'dine-in': 0.0002, 
    'delivery': 0.001, 
    'pick-up': 0.0
}

size_type = [
    {"size": "24oz", "price": 89.00},
    {"size": "32oz", "price": 97.00},
    {"size": "40oz", "price": 110.00},
]
orders = []
subtotal = 0

def displayMenu():
    while True: 
        print("\nFlavors: ")
        for i, coffee in enumerate(coffee_menu, start=1):
           print(f"[{i}] {coffee['flavor']}: ${coffee['price']:.2f}")
        try:
            flavorChoice = int(input("Flavor: "))
            
            if  1 <= flavorChoice <= len (coffee_menu):
                chosenFlavor = coffee_menu[flavorChoice]
                return chosenFlavor
            else:
                print("Invalid choice. Please select a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    

def transaction():
    while True:
        print("Transaction Type:")
        for transaction in trans_type.keys():
            print(f"-{transaction} ")
        transactionChoice = input("Choice: ")
        
        if transactionChoice in trans_type:
            return transactionChoice, trans_type[transactionChoice]
        else:
            print("Invalid. Please Try Again.")

def displaySize():
    while True:

        print("Size:")
        for size in size_type:
            print(f"{size} : Php{size_type[size]:.2f}")
        sizeChoice = input("Size: ").strip()

        if sizeChoice in size_type:
            return sizeChoice, size_type[sizeChoice]
        else:
            print("Invalid choice.")

def quantityChoice():
    return int(input("Quantity:"))


def calculateSubtotal(order):
    return(order["flavorPrice"] + order ["sizePrice"] * order["quantity"])

def takeOrder(transaction_charge):
    global subtotal

    
    chosenFlavor = displayMenu()
    chosenSize, sizePrice = displaySize()
    quantity = quantityChoice()

    order = {
        "flavor": chosenFlavor["flavor"],
        "flavorPrice": chosenFlavor["price"],
        "size": chosenSize,
        "sizePrice": sizePrice,
        "quantity": quantity
        
    }
    orders.append(order)



    order_total = calculateSubtotal(order)
    subtotal += order_total
    print(f"\nSubtotal: Php{subtotal:.2f}" )

transactionChoice, transaction_charge = transaction()


while True:
    
    takeOrder(transaction_charge)
    print("-------------------------------")
    addMore = input("Add order(s), y or n: ")
    if addMore.lower().strip() != "y":
        break

print("\nOrders:")
for order in orders:
    print(f"({order['quantity']}) {order['flavor']} {order['size']} - "
          f"Php{order['flavorPrice']:.2f} + Php{order['sizePrice']:.2f} each")

other_charges = subtotal * transaction_charge
final_total = subtotal + other_charges

print("\nSubtotal: Php{:.2f}" .format(subtotal))
print("Other Charges: Php{:.2f}".format(other_charges))
print("Total: Php{:.2f}".format(final_total))
print("\nThank you come again!")