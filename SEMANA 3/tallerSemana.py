
# Inventory is a list of product dictionaries
inventory = []


# Function to add a new product
def addProduct():
    name = input("Enter the product name: ").lower()
    if not name:
        print("The name cannot be empty.")
        return
    for product in inventory:
        if product["name"] == name:
            print("This product already exists.")
            return
    try:
        price = float(input("Enter the product price: "))
        quantity = int(input("Enter the product quantity: "))
        if price <= 0 or quantity <= 0: ##price and quantity input validation
            print("Price and quantity must be greater than 0.")
            return
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    inventory.append({"name": name, "price": price, "quantity": quantity})## we use the append method to add the product to the list
    print("Product added successfully.")


# Function to view a product
def consultProduct():
    name = input("Enter the product name to view: ").lower()
    for product in inventory:
        if product["name"] == name.lower(): ##for product in inventory: ##check if the product exists in the dictionary
            print("Product found.")
            print(f"Name: {product['name']}, Price: {product['price']}, Quantity: {product['quantity']}")
            return
    else:
        print("Product not found.")

# Function to update a product's price
def updatePrice():
    name = input("Enter the product name to update: ").lower()
    product = next((product for product in inventory if product["name"] == name), None)#next function to find the product and return it, if not found return None
    if product:
        try:
            newPrice = float(input("Enter the new price: "))
            if newPrice <= 0:
                print("Price must be greater than 0.")
                return
            product["price"] = newPrice ##we search the product in the dictionary using the name as key and assign the new price using the price key
            print("Price updated successfully.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")
    else:
        print("Product not found.")

# Function to delete a product
def deleteProduct():
    name = input("Enter the product name to delete: ").lower()
    product = next((product for product in inventory if product["name"] == name), None)##next function to find the product and return it, if not found return None
    if product:
        confirm = input("Are you sure you want to delete it? (yes/no): ").lower()
        if confirm == "yes":
            inventory.remove(product)## we search the product in the dictionary using the name as key and remove it with the remove method
            print("Product deleted.")
        else:
            print("Deletion canceled.")
    else:
        print("Product not found.")

# Function to list all products
def listProducts():
    if not inventory:
        print("No products in inventory.")
    else:
        for i, product in enumerate(inventory, start=1): ## Start enumeration from 1
            print(f"{i}. Name: {product['name']}, Price: {product['price']}, Quantity: {product['quantity']}")

# Lambda function to calculate total inventory value
calculateTotal = lambda: sum(p["price"] * p["quantity"] for p in inventory)##P is a variable that represents the product in the inventory, we use the sum function to calculate the total value of the inventory, we use the lambda function to create a function that calculates the total value of the inventory, we use the p["price"] * p["quantity"] to calculate the total value of each product in the inventory and we use the sum function to calculate the total value of all products in the inventory

# MAIN MENU
while True:
    print("\n--- WELCOME TO MAYE`S STORE ---")
    print("\n----------------MENU --------------")
    print("Please choose an option:")
    print("1. Add product")
    print("2. View product")
    print("3. Update price")
    print("4. Delete product")
    print("5. List all products")
    print("6. Calculate total inventory value")
    print("7. Exit")

    try:
        option = int(input("Choose an option (1-7): "))
    except ValueError:
        print("Invalid option. Please enter a number.")
        continue

    if option == 1:
        addProduct()
    elif option == 2:
        consultProduct()
    elif option == 3:
        updatePrice()
    elif option == 4:
        deleteProduct()
    elif option == 5:
        listProducts()
    elif option == 6:
        print("Total inventory value:", calculateTotal())
    elif option == 7:
        print("Thank you for using the inventory system.")
        break
    else:
        print("Invalid option. Please choose between 1 and 7.")
