##INVENTARIO DIGITAL
##Debe contener un CRUD, calcular el valor total del inventario y listar los productos
##Para calcular el total del inventario se debe usar una funcion lambda


##Creacion de diccionario
inventory={}
##Definicion metodo para añadir productos
def addProduct():
    name=input("Please, enter the product name: ")
    price=float(input("Please, enter the product price: "))
    cant=int(input("Please, enter the product quantity: "))
    inventory[name]={"name": name, "price":price, "cant":cant} ##llamamos al diccionario y le asignamos el name del product como clave, luego le asignamos un diccionario con el name del product, price y cant
    print("¡Product added successfully!") ##imprimimos el mensaje de exito
    
##METODO CONSULTAR
def consultProduct():
    name=input("Please, enter the name of the product to be queried: ")
    if name in inventory: ##verificamos si el product existe en el diccionario
        print("Product found") ##imprimimos el mensaje de exito
        print(f"Name: {inventory[name]['name']}, Price: {inventory[name]['price']}, Quantity: {inventory[name]['cant']}")##imprimimos el product, price y cant,usamos el name como clave para acceder al diccionario
    else:
        print("Product not found") ##si no existe el product imprimimos el mensaje de error

##METODO ACTUALIZAR PRECIO
def updatePrice():
    name=input("Please, enter the product el name del product to update: ")
    if name in inventory:
        price=float(input("Please, enter the new price of the product: "))
        inventory[name]["price"]=price ## BUscamos en el diccionario el product usando el name como la clave y le asignamos el nuevo price usando la clave price
        print("Price updated successfully") ##imprimimos el mensaje de exito
    else:
        print("Product not found") ##si no existe el product imprimimos el mensaje de error
        
##METODO ELIMINAR PRODUCTOS
def deleteProduct():
    name=input("Please, enter the name of the product to be deleted: ")
    if name in inventory:
        inventory.pop(name) ##buscamos el product en el diccionario usando el name como la clave y lo eliminamos con el metodo pop
        print("Price deleted successfully") ##imprimimos el mensaje de exito
    else:
        print("Product not found") ##si no existe el product imprimimos el mensaje de error

##METODO LISTAR PRODUCTOS
def listProduct():
    if not inventory: ##verificamos si el diccionario esta vacio
        print("No products registered") ##imprimimos el mensaje de error
    else: 
        for i, name in enumerate(inventory.keys(), start=1): ##enumerate nos permite recorrer el diccionario y obtener el indice y el name del product, el . keys nos permite obtener las claves del diccionario y el start=1 nos permite empezar desde 1
            print(f"{i}. name: {inventory[name]['name']}, price: {inventory[name]['price']}, quantity: {inventory[name]['cant']}")
        print("Products listed successfully") ##imprimimos el mensaje de exito
    
##METODO CALCULAR TOTAL FUNCION LAMBDA
calculateTotal = lambda: sum(map(lambda x: x["price"] * x["cant"], inventory.values())) ##usamos la funcion map para recorrer el diccionario y multiplicar el price por la cant, luego usamos la funcion sum para sumar todos los valores
print("|The total inventory is: ", "|" ,calculateTotal() ,"|")

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
        print("Invalid option, please enter a number") ##imprimimos el mensaje de error
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


