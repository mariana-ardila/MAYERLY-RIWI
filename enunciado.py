num=int(input("Por favor ingresa un numero: "))



        
if num %5==0 and num %3==0:
    print ("FizzBuzz")
elif num %3==0:
    print("Fizz")
elif num %5==0:
    print("Buzz")

else:
    print(f"El numero es: {num}")