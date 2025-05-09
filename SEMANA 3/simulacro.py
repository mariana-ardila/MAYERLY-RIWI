## Gestión de Inventario de una Librería 

inventory=[
    {"title": "One Hundred Years of Solitude", "price": 100.000, "quantity": 100},
    {"title": "Gone with the Wind", "price": 30.000, "quantity": 50},
    {"title": "Me before you", "price": 15.000, "quantity": 30},
    {"title": "Blindness", "price": 55.000, "quantity": 42},
    {"title": "Twilight", "price": 30.000, "quantity": 5}
]


##add books method
def addinventory ():
    tittle=input("Please, enter the tittle of the book: ")
    price=float(input("Please, enter the price of the book:"))
    quantity=int(input("Please, enter de quantity of the book:"))
    inventory.append({"title":tittle, "price":price, "quantity": quantity})## we use the append method to add the book to the list
    
    
    ##number input validation
    if price <0:
        print("The price must be greater than 0")
        return
    elif quantity <0:
        print("The quantity must be greater than 0")
        return
    else:
        print("¡Book added successfully!")
       
##consult book method
def consultLibrery():
    tittle=input("Please,enter the tittle of the book to consult:")
    for book in inventory: ##check if the book exists in the dictionary
       if book["title"].lower()== tittle.lower(): ##we use the lower method to convert the book to lowercase and compare it with the input
            print("The book has been found")
            print(f"book: {book['title']}, Price: {book['price']}, Quantity: {book['quantity']}") ## print the tittle, price and quantity of the book, we use the tittle as key to access the dictionary
            return
    else:
        print("Book not found in the inventory")  

##update price method
def updatePrice():
    tittle=input("Please, enter the tittle of the book to updte: ")
    for book in inventory: ##check if the book exists in the dictionary
        if book["title"].lower() == tittle.lower(): ##we use the lower method to convert the tittle to lowercase and compare it with the input
            print("Book found")
            price=float(input("Please, enter the new price of the book: "))
        if price >0: ##price input validation
            book["price"]=price ##we search the book in the dictionary using the tittle as key and assign the new price using the price key
            print("Price updated successfully")
        else:
            print("The price must be greater than 0")
        return
    else:
        print("Book not found in the inventory")
        


##delete book method
def deleteBook():
    tittle=input("Please, enter the tittle of the book to be deleted: ")
    for book in inventory:
        if book["title"].lower()== tittle.lower(): ##we use the lower method to convert the tittle to lowercase and compare it with the input
            print("The book exists in the inventory")
            delete=input("Do you want to delete the book? (yes/no): ")
            if delete.lower()=="yes":
                inventory.remove(book) ###we search the book in the dictionary using the tittle as key and remove it with the remove method
                print(f"Book {book['title']} deleted successfully")
                return
            else:
                print("Book not deleted")
                return
    else:
        print("Book not found in the inventory")

##calculate total inventory method
def calculateTotal():
    total=0 ##initialize the total variable
    for book in inventory: ##we use the values method to get the values of the dictionary
        total+=book["price"]*book["quantity"] ##we multiply the price by the quantity and add it to the total
    return total ##return the total
    print(f"The total inventory is: ${calculateTotal():.2f}") ##print the total inventory with 2 decimal places
    

##list books method
def listBooks():
    if not inventory:
        print("No books registered")
    else: 
        for i, book in enumerate(inventory, start=1): ##we use enumerate to iterate over the dictionary and get the index and the book of the book, the .keys method allows us to get the keys of the dictionary and the start=1 allows us to start from 1
            print(f"{i}. Title: {book['title']}, Price: {book['price']}, Quantity: {book['quantity']}") ## print the tittle, price and quantity of the book, we use the tittle as key to access the dictionary
        print("Books listed successfully") ##print the success message
    print("Thanks for visiting us") ##print the success message
    
    
##menu
while True:
    print("WELCOME TO THE LIBRARY INVENTORY")
    print("1. Add book")
    print("2. Consult book")
    print("3. Update price")
    print("4. Delete book")
    print("5. List books")
    print("6. Calculate total inventory")
    print("7. Exit")
    
    try:
        option=int(input("Please, enter an option: "))
    except ValueError:
        print("Invalid option, please enter a number") ##print the error message
        continue
    
    if option==1:
            addinventory()
    elif option==2:
            consultLibrery()
    elif option==3:
            updatePrice()
    elif option==4:
            deleteBook()
    elif option==5:
            listBooks()
    elif option==6:
            print("The total inventory is: ", calculateTotal())
    elif option==7:
            print("Thanks for visiting us")
            break
    else:
            print("Invalid option, please enter a number")
            

    
