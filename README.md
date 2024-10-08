# The Variety Food Truck Ordering System - Python Challenge

## Overview
This project is an interactive ordering system for The Variety Food Truck, built using Python. The program allows customers to browse through a menu, place their orders, and receive a printed receipt with the total price of all items ordered.

The main file in this repository is [`menu.py`](https://github.com/jsaintfleur/python-challenge-1/blob/main/menu.py), which contains the Python code for running the ordering system.

## Features
- A menu with various categories such as **Snacks**, **Meals**, **Drinks**, and **Dessert**.
- **Input validation** for selecting menu items and quantities to ensure correct inputs.
- The ability to place multiple orders and receive a formatted receipt at the end of the order.
- **Dynamic column width calculation** to ensure proper alignment of items in the receipt.
- Calculates the **total cost** of all items ordered, displayed clearly on the receipt.

## File Structure
- `menu.py`: This file contains the main logic for the ordering system, including the menu, input prompts, order processing, and receipt generation.

## Getting Started

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/jsaintfleur/python-challenge-1.git
    ```

2. Navigate to the cloned repository:

    ```bash
    cd python-challenge-1
    ```

3. Run the program:

    ```bash
    python menu.py
    ```

## How It Works
1. The program starts by greeting the customer and presenting the main menu categories.
2. The customer selects a category and then chooses an item from that category.
3. The customer inputs the quantity they wish to order.
4. The system prompts whether the customer wants to continue ordering or finalize the order.
5. Once the customer finishes ordering, a receipt with all items and their total cost is printed.

## Example Output

```plaintext
Welcome to The Variety Food Truck.

From which menu would you like to order? 
1: Snacks
2: Meals
3: Drinks
4: Dessert
Type menu number: 1

You selected Snacks

What Snacks item would you like to order?

Item # | Item name                | Price
-------|--------------------------|-------
1      | Cookie                   | $0.99
2      | Banana                   | $0.69
3      | Apple                    | $0.49
4      | Granola bar              | $1.99

Enter item number: 1

How many Cookie would you like? 2

Added 2 x Cookie to your order.

Would you like to keep ordering? (Y)es or (N)o: n

Thank you for your order.

This is what we are preparing for you.

Item name                 | Price  | Quantity | Line Total
--------------------------|--------|----------|-----------
Cookie                    | $0.99  |        2 | $1.98     

----------------------------------------
Grand Total: $1.98


## Additional Information

- The system validates user input at every step, ensuring that incorrect inputs are handled gracefully.
- The receipt format dynamically adjusts to the length of the longest item names, prices, and quantities, ensuring consistent presentation.
