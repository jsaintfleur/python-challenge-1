# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# Initialize an empty list to store the order
order = []

# Function to print the receipt dynamically with alignment
def print_receipt(order):
    print("\nThis is what we are preparing for you:\n")
    print("Item name                 | Price  | Quantity")
    print("--------------------------|--------|----------")

    # Loop through the items in the customer's order
    total_cost = 0
    for item in order:
        item_name = item["Item name"]
        price = item["Price"]
        quantity = item["Quantity"]

        # Calculate the number of spaces for each column to ensure proper alignment
        num_item_spaces = 26 - len(item_name)
        item_spaces = " " * num_item_spaces

        price_spaces = " " * (7 - len(f"${price:.2f}"))
        quantity_spaces = " " * (8 - len(str(quantity)))

        # Print the item details in the required format
        print(f"{item_name}{item_spaces}| ${price:.2f}{price_spaces}| {quantity}{quantity_spaces}")

        total_cost += price * quantity

    print(f"\nTotal: ${total_cost:.2f}")

# Function to allow modification of an order
def modify_order(order):
    print("\nHere are the items in your order:")
    for idx, item in enumerate(order, start=1):
        print(f"{idx}: {item['Item name']} (Quantity: {item['Quantity']}, Price per item: ${item['Price']})")

    item_to_modify = input("\nEnter the number of the item you'd like to modify, or type 'cancel' to return: ")

    if item_to_modify.lower() == 'cancel':
        return

    if item_to_modify.isdigit() and 1 <= int(item_to_modify) <= len(order):
        idx = int(item_to_modify) - 1
        action = input(f"Would you like to 'remove' or 'update' the quantity of {order[idx]['Item name']}? ").lower()

        if action == "remove":
            order.pop(idx)
            print("Item removed from your order.")
        elif action == "update":
            new_quantity = input(f"Enter the new quantity for {order[idx]['Item name']}: ")
            if new_quantity.isdigit():
                order[idx]["Quantity"] = int(new_quantity)
                print(f"Updated {order[idx]['Item name']} to {new_quantity} quantity.")
            else:
                print("Invalid quantity. No changes were made.")
        else:
            print("Invalid action. Returning to order.")
    else:
        print("Invalid item selection.")

# Launch the store and present a greeting to the customer
print("Welcome to The Variety Food Truck.")

# Customers may want to order multiple items, so let's create a continuous loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("\nFrom which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first-level dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"\nYou selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"\nWhat {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("\nItem # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + " - " + key2)
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2:.2f}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value:.2f}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1

            # 2. Ask customer to input menu item number
            menu_selection = input("\nEnter the item number you wish to order: ")

            # 3. Check if the customer typed a number
            if menu_selection.isdigit():
                menu_selection = int(menu_selection)

                # 4. Check if the menu selection is in the menu items
                if menu_selection in menu_items:
                    # Store the item name and price as variables
                    selected_item = menu_items[menu_selection]
                    item_name = selected_item["Item name"]
                    item_price = selected_item["Price"]

                    # Ask the customer for the quantity of the menu item
                    quantity = input(f"\nHow many {item_name}(s) would you like to order? (Default is 1): ")

                    # Check if the quantity is a number, default to 1 if not
                    if not quantity.isdigit():
                        quantity = 1
                    else:
                        quantity = int(quantity)

                    # Add the item name, price, and quantity to the order list
                    order.append({
                        "Item name": item_name,
                        "Price": item_price,
                        "Quantity": quantity
                    })

                    print(f"\nAdded {quantity} {item_name}(s) to your order.")
                else:
                    # Tell the customer that their input isn't valid
                    print("\nThat item number is not on the menu.")
            else:
                # Tell the customer they didn't select a valid number
                print("\nInvalid selection. Please enter a valid number.")
        else:
            # Tell the customer they didn't select a menu option
            print(f"\n{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("\nYou didn't select a number.")

    # Ask the customer if they would like to keep ordering or modify their order
    keep_ordering = input("\nWould you like to (C)ontinue ordering, (M)odify your order, or (F)inish? ").lower()

    if keep_ordering == 'f':
        # Print the receipt and end the order
        print("\nThank you for your order.")
        print_receipt(order)
        place_order = False
    elif keep_ordering == 'm':
        # Modify the existing order
        modify_order(order)
    elif keep_ordering != 'c':
        print("\nInvalid input. Please enter 'C', 'M', or 'F'.")
