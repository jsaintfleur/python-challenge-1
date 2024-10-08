# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": 0.99,
        "Banana": 0.69,
        "Apple": 0.49,
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

# 1. Set up order list. Order list will store a list of dictionaries for menu item name, item price, and quantity ordered.
order_list = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level dictionary items in menu).
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
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
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
            menu_selection = input("\nEnter item number: ")

            # 3. Check if the customer typed a number
            if menu_selection.isdigit():
                menu_selection = int(menu_selection)

                # 4. Check if the menu selection is in the menu items
                if menu_selection in menu_items:
                    # Store the item name as a variable
                    item_name = menu_items[menu_selection]["Item name"]
                    item_price = menu_items[menu_selection]["Price"]

                    # Ask the customer for the quantity of the menu item
                    quantity = input(f"How many {item_name} would you like? ")

                    # Check if the quantity is a number, default to 1 if not
                    if not quantity.isdigit():
                        quantity = 1
                    else:
                        quantity = int(quantity)

                    # Add the item name, price, and quantity to the order list
                    order_list.append({
                        "Item name": item_name,
                        "Price": item_price,
                        "Quantity": quantity
                    })

                    print(f"\nAdded {quantity} x {item_name} to your order.")
                else:
                    # Tell the customer they didn't select a valid menu option
                    print(f"{menu_selection} was not a valid menu option.")
            else:
                # Tell the customer they didn't select a number
                print("You didn't select a number.")
        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ").lower()

        # Check the customer's input
        if keep_ordering == 'y':
            # Keep ordering
            place_order = True
            break
        elif keep_ordering == 'n':
            # Complete the order
            print("Thank you for your order.")
            place_order = False
            break
        else:
            # Tell the customer to try again
            print("Please try again by typing 'Y' or 'N'.")

# Print out the customer's order
print("\nThis is what we are preparing for you.\n")

# Calculate column widths based on the longest values dynamically
def calculate_column_widths(order_list):
    max_name_length = max(len(item["Item name"]) for item in order_list)
    max_price_length = max(len(f"${item['Price']:,.2f}") for item in order_list)
    max_quantity_length = max(len(str(item["Quantity"])) for item in order_list)
    max_total_length = max(len(f"${item['Price'] * item['Quantity']:,.2f}") for item in order_list)
    return max(max_name_length, 10), max(max_price_length, 6), max(max_quantity_length, 8), max(max_total_length, 10)

# Get column widths dynamically
name_col_width, price_col_width, quantity_col_width, total_col_width = calculate_column_widths(order_list)

# Print header for the order receipt
header = f"{'Item name':<{name_col_width}} | {'Price':>{price_col_width}} | {'Quantity':>{quantity_col_width}} | {'Line Total':>{total_col_width}}"
print(header)
print("-" * len(header))

# Loop through the items in the customer's order to print each line
for item in order_list:
    item_name = item["Item name"]
    price = item["Price"]
    quantity = item["Quantity"]
    line_total = price * quantity

    # Print each line item with proper alignment
    line = (
        f"{item_name:<{name_col_width}} | "
        f"${price:>{price_col_width - 1},.2f} | "
        f"{quantity:>{quantity_col_width}} | "
        f"${line_total:>{total_col_width - 1},.2f}"
    )
    print(line)

# Calculate the grand total using list comprehension
grand_total = sum(item["Price"] * item["Quantity"] for item in order_list)
print("\n" + "-" * len(header))
print(f"Grand Total: ${grand_total:,.2f}".rjust(len(header)))
