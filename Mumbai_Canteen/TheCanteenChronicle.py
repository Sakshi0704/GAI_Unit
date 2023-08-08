# Snack inventory will be stored as a dictionary where the keys are snack IDs and values are dictionaries containing snack details.
snack_inventory = {}

# Sales records will be stored as a list of dictionaries, each representing a sale with snack ID and quantity.
sales_records = []

def add_snack():
    snack_id = input("Enter snack ID: ")
    snack_name = input("Enter snack name: ")
    price = float(input("Enter price: "))
    snack_inventory[snack_id] = {"name": snack_name, "price": price, "available": True}
    print(f"Snack '{snack_name}' added to the inventory.")

def remove_snack():
    snack_id = input("Enter snack ID: ")
    if snack_id in snack_inventory:
        snack_name = snack_inventory[snack_id]["name"]
        del snack_inventory[snack_id]
        print(f"Snack '{snack_name}' removed from the inventory.")
    else:
        print("Snack not found in the inventory.")

def update_availability():
    snack_id = input("Enter snack ID: ")
    if snack_id in snack_inventory:
        new_availability = input("Is the snack available? (yes/no): ").lower()
        snack_inventory[snack_id]["available"] = new_availability == "yes"
        print("Availability updated.")
    else:
        print("Snack not found in the inventory.")

def record_sale():
    snack_id = input("Enter snack ID: ")
    if snack_id in snack_inventory:
        if snack_inventory[snack_id]["available"]:
            quantity = int(input("Enter quantity sold: "))
            snack_name = snack_inventory[snack_id]["name"]
            sales_records.append({"snack_id": snack_id, "quantity": quantity})
            print(f"Sale recorded: {quantity} {snack_name}(s) sold.")
            snack_inventory[snack_id]["available"] = False
        else:
            print("Snack is not available.")
    else:
        print("Snack not found in the inventory.")

def display_inventory():
    print("Snack Inventory:")
    for snack_id, snack_details in snack_inventory.items():
        availability = "Available" if snack_details["available"] else "Not Available"
        print(f"ID: {snack_id}, Name: {snack_details['name']}, Price: {snack_details['price']}, Availability: {availability}")

def display_sales_records():
    print("Sales Records:")
    for sale in sales_records:
        snack_id = sale["snack_id"]
        quantity = sale["quantity"]
        snack_name = snack_inventory[snack_id]["name"]
        print(f"Snack: {snack_name}, Quantity Sold: {quantity}")

def main():
    while True:
        print("\nWelcome to Mumbai Munchies: The Canteen Chronicle!")
        print("1. Add Snack\n2. Remove Snack\n3. Update Availability\n4. Record Sale\n5. Display Inventory\n6. Display Sales Records\n7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_snack()
        elif choice == "2":
            remove_snack()
        elif choice == "3":
            update_availability()
        elif choice == "4":
            record_sale()
        elif choice == "5":
            display_inventory()
        elif choice == "6":
            display_sales_records()
        elif choice == "7":
            print("Thank you for using Mumbai Munchies!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
