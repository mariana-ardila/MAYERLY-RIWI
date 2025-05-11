##INVENTARIO DIGITAL
##Debe contener un CRUD, calcular el valor total del inventario y listar los productos
##Para calcular el total del inventario se debe usar una funcion lambda


##Create a dictionary to store the products
inventory={}


##Method to add products
def addProduct():
    name = input("Please, enter the product name: ").lower() # ask for the product name
    if not name.isalpha():  # name input validation ##ISALFA method to check if the name is a string
        print("Invalid name, please enter a valid string (letters only)")
        return
    if name == "":  # name input validation
        print("The name cannot be empty")
        return
    # number input validation for price
    try:
        price = float(input("Please, enter the product price: "))
        if price <= 0:  # price input validation
            print("The price must be a positive number")
            return
    except ValueError:
        print("Invalid price, please enter a valid number")
        return
    # number input validation for quantity
    try:
        cant = int(input("Please, enter the product quantity: "))
        if cant <= 0:  # quantity input validation
            print("The quantity must be a positive integer")
            return
    except ValueError:
        print("Invalid quantity, please enter a valid integer")
        return

    inventory[name] = {"name": name, "price": price, "cant": cant}  # create the product in the dictionary
    print("¡Product added successfully!")

#Method to consult products
def consultProduct():
    name=input("Please, enter the name of the product to be queried: ")
    if name in inventory: ##verify if the product exists in the dictionary
        print("Product found")
        print(f"Name: {inventory[name]['name']}, Price: {inventory[name]['price']}, Quantity: {inventory[name]['cant']}")#print the product information
    else:
        print("Product not found") ##if the product does not exist, print an error message

#Method to update the price of a product
def updatePrice():
    name=input("Please, enter the product el name del product to update: ")
    if name in inventory:
        print("Product found")
        price=float(input("Please, enter the new price of the product: "))
        if price >0: ##price input validation
            inventory[name]['price']=price ##we search the product in the dictionary using the name as key and assign the new price using the price key
            print("Price updated successfully")
        else:
            print("The price must be greater than 0")
        return
    else:
        print("Product not found") 
        
#Method to delete a product
def deleteProduct():
    name=input("Please, enter the name of the product to be deleted: ")
    if name in inventory: ##verify if the product exists in the dictionary
        print(inventory[name]) ##print the product information
        confirm=input("Are you sure you want to delete this product? (yes/no): ") ##ask for confirmation to delete the product
        if confirm.lower() == "yes".lower(): ##if the user confirms, delete the product
            inventory.pop(name) ##focus on the product in the dictionary using the name as the key and delete it
            print("Product deleted successfully")
        
    else:
        print("Product not found") 

##Method to list products
def listProduct():
    if not inventory: #verify if the inventory is empty
        print("No products registered") 
    else: 
        for i, name in enumerate(inventory.keys(), start=1): ##enumerate the dictionary to get the index and the name of the product
            print(f"{i}. name: {inventory[name]['name']}, price: {inventory[name]['price']}, quantity: {inventory[name]['cant']}")
        print("Products listed successfully") ##imprimimos el mensaje de exito
    
##Method to calculate the total of the inventory
calculateTotal = lambda: sum(map(lambda x: x["price"] * x["cant"], inventory.values())) ##calculate the total of the inventory using a lambda function and the map function to iterate over the values of the dictionary and multiply the price by the quantity
print("The total inventory is: " ,calculateTotal() )

##MENU
while True: 
    print ("WELCOME TO THE DIGITAL INVENTORY")
    print ("1. Add product")
    print ("2. Consult product")
    print ("3. Update price")
    print ("4. Delete product")
    print ("5. List products")
    print ("6. Calculate total inventory")
    print ("7. Exit")

    try: 
        option=int(input("Please, enter an option: "))
    except ValueError:
        print("Invalid option, please enter a number") 
        continue
    if option==1:
        addProduct()
    elif option==2:
        consultProduct()
    elif option==3:
        updatePrice()
    elif option==4:     
        deleteProduct()
    elif option==5: 
        listProduct()
    elif option==6:
        print("The total inventory is: ", calculateTotal())
    elif option==7:
        print("Thanks for visiting us")
        break
    else:
        print("Invalid option, please enter a number")


