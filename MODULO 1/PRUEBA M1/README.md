###INPUT DATA IN THE LIST

##We start by burning the list with data already stored in a dictionary
    "name": "Rice", "price": 100.000, "quantity": 100
    "name": "Sugar", "price": 30.000, "quantity": 50
    "name": "Salt", "price": 15.000, "quantity": 30
    "name": "Lemon", "price": 55.000, "quantity": 42
    "name": "Bread", "price": 30.000, "quantity": 5

###WE CREATE ALL TRE CRUD 
-addProduct Method: In this method, the user is asked to enter all the product data, such as name, 
price and quantity, in order to create the product within the list.
The respective validations of the input data are made, using an if

-consultProduct Method: We ask the user to enter the name of the product they want to consult.
We use a for loop to traverse my list. If the product in my index position is equal to the one the user found, a success message is printed and all product data continues to be displayed.

-updateProdcut Method: The user enters the name of the product for which they want to modify its price, it is validated if the product exists in the dictionary using a for loop, which what it does is go through my list, if the product exists we continue with the next step where we use a conditional if, what this does is compare my product in the index position with the entered data, if they are equal it prints a message that the product was found and continues asking the user to enter the new price, this also has its conditions, if the number entered is greater than 0 it continues assigning that new price to my key.

-deleteProduct Methos: 