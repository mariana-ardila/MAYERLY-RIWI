inventory=[
    {"name": "Rice", "price": 3.000, "quantity": 100},
    {"name": "Sugar", "price": 30.000, "quantity": 50},
    {"name": "Salt", "price": 15.000, "quantity": 30},
    {"name": "Lemon", "price": 55.000, "quantity": 42},
    {"name": "Bread", "price": 30.000, "quantity": 5}
]


#--------------------------------------------------------------------------------------------------------

#Add product method

def addProduct ():
    #We request product entry data
    name=input("Please, enter the name of product: ")
    price=float(input("Please, enter the price of product: "))
    quantity=int(input("Please, enter the quantity of product: "))
    #we store the data entered in the list using the append method 
    inventory.append({"name": name, "price": price, "quantity": quantity})

    ##number input validation
    if price <0:
        print("The price must be greater than 0")
        return
    elif quantity <0:
        print("The quantity must be greater than 0")
        return
    else:
        print("¡Product added successfully!")

print(addProduct)

#-----------------------------------------------------------------------------------------------------------

#Consult product method 

def consultProduct ():
    name=input("Please, enter the name of the product focus: ")
    #check if the product exists in the dictionary used For-Else
    for product in inventory:
        if product["name"].lower()==name.lower():
            print("Product found")
            #Print dates of the product
            print(f"Product: {product["name"]}, Price: {product["price"]}, Quantity: {product["quantity"]}")
            return
    else:
        print("Product no found in the inventory")

#------------------------------------------------------------------------------------------------------------

def updateProduct ():
    name=input("Please enter the name of the product you wish to update: ")
    #Check if the product exists in the dictionary used For-Else
    for product in inventory:
        #We check if the product name in the position is the same as the entered name.
        if product["name"].lower()==name.lower():
            print("Product found")
            newPrice=float(input("Please, enter the new price of product: $"))

            #price input validation
        if newPrice >0: ##price input validation
            ##We search the product in the dictionary using the name as key and assign the new price using the price key
            product["price"]=newPrice 
            print("Price updated successfully")
        else:
            print("The price must be greater than 0")
        return
    else:
        print("Product not found in the inventory")

#-------------------------------------------------------------------------------------------------------------

def deleteProduct():
    name=input("Please, enter the name of the product you wish to delete: ")
    for product in inventory:
        if product["name"].lower()==name.lower():
            print("The product exists in the inventory")
            delete=input("Do you want to delete the product? (yes/no): ")
            if delete.lower()=="yes":
                ###we search the product in the dictionary using the name as key and remove it with the remove method
                inventory.remove(product) 
                print(f"Product: {product["name"]} deleted successfully")
                return
            else:
                print("Product not deleted")
                return
    else:
        print("Product not found in the inventory")

#-------------------------------------------------------------------------------------------------------------------

def calculateTotal ():
    total=0
    for product in inventory:
        #we calculate the total     
        total+=product["price"]*product["quantity"]
        return total
    #print the total with 2 decimal used .2f
    print(f"The total inventory is: ${calculateTotal():.2f}")

#-------------------------------------------------------------------------------------------------------------------

##MENU

while True: 
    print("\n------WELCOME TO MAYE'S STORE INVENTORY-----------")
    print("Please choose an option:")
    print("1. Add product")
    print("2. Consult product")
    print("3. Update price")
    print("4. Delete product")
    print("5. Calculate total inventory value")
    print("6. Exit")

    try:
        option = int(input("Choose an option (1-6): "))
    except ValueError:
        print("Invalid option. Please enter a number.")
        continue


    if option==1:
        addProduct()
    
    if option==2:
        consultProduct()

    if option==3:
        updateProduct()

    if option==4:
        deleteProduct()
    
    if option==5:
        print(f"The total inventory is: ${calculateTotal()}")

    if option==6:
        print("Tanks for you visit")







    

