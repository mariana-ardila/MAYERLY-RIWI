###INPUT DATA IN THE LIST

##We start by burning the list with data already stored in a dictionary
    "name": "Rice", "price": 100.000, "quantity": 100
    "name": "Sugar", "price": 30.000, "quantity": 50
    "name": "Salt", "price": 15.000, "quantity": 30
    "name": "Lemon", "price": 55.000, "quantity": 42
    "name": "Bread", "price": 30.000, "quantity": 5

###WE CREATE ALL TRE CRUD 
-addProduct Method: I create this function with three parameters, name, price and quantity, I do this to put the input in the menu so that my function is as clean as possible, once my menu requests the 3 input data (name, price and quantity) what I do is add them to my list using the append function, and finally I add a success message.
I validate the input data using conditionals, so that the price and quantity are not negative numbers, I set the condition that it must be greater than zero.

-consultProduct Method: We ask the user to enter the name of the product they wish to view.
We use a for loop to iterate through the list. If the product at my index position matches the one the user found, a success message is displayed and all product data continues to be displayed. I request the input data in the menu to keep the function as clean as possible.

-updateProdcut Method: the user enters the name of the product for which they want to modify its price, it is validated if the product exists in the dictionary through a for loop, which what it does is go through my list, if the product exists we continue with the next step where we use a conditional if, what this does is compare my product in the index position with the entered data, if they are equal it prints a message that the product was found and continues asking the user to enter the new price, this also has its conditions, if the number entered is greater than 0 it continues assigning that new price to my key. I also use a Try except to validate the input data by the user.

-deleteProduct Method: Validation is made that the data entered by the user exists within my dictionary, I do this using a for loop that goes through my list until it finds the index of the data entered, after this I compare it using a conditional if, if my data in my index position is equal to the data entered I print a product found message and proceed to ask the user if they are sure to delete the data, if the answer is "yes" it is deleted using the remove function and a message is printed showing which product was deleted. In this function, as in almost all, I put the input data as parameters in the function to later be called and used in the menu.

-calculateTotal: A variable total initialized to zero is created, which will contain the entire inventory total process. I use a for loop that will allow me to go through my list. I rename my total variable by assigning it the procedure, where I specify that total will be equal to the sum of my index (product) in the "price" key * my index in the "quantity" key and return the variable sum.

MENU

I create the menu using a While True statement, which means that while it's true, everything in the menu is executed. I also use a try except statement to catch errors like "if the user enters a number that isn't in the menu." In case 1, I use an error message if the user enters a negative price or quantity. In the other cases, I only request the input data and call my function with its respective parameters. In case 5, I print my inventory total and ask it to show me the result with only 2 decimal places. I do this using .2f.


---------------------
To use my project, it is only necessary to run it in a development environment that connects Python, nothing else is necessary since the data is shown to me via the console (terminal).