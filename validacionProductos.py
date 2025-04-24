
##DECLARACION VARIABLES 
nombreProducto=str(input("Ingresa el nombre del producto: "))

precioProducto=float(input("Ingresa el precio del producto: "))

cantidadProducto=int(input("Ingrese la cantidad de productos: "))

descuentoProducto=float(input("¿Que cantidad de decuento desea aplicar?: "))

if precioProducto>0:
    print("Los datos ingresados no son correctos")
if cantidadProducto>0:
    print("Los datos ingresados no son correctos")
##Validacion del precio-cantidad sean positivos 
if precioProducto and cantidadProducto >0 :

## operacion para calcular el total de la compra sin descuento
    totalCompra= precioProducto*cantidadProducto
    print("El total de la compra es: " , totalCompra)


##Validacion para que el descuento este en el rango de 0-100
if 0<= descuentoProducto<=100:
##Operacion para calcular el porcentaje aplicado 
    descuento= totalCompra *(descuentoProducto/100)
    print("el descuento aplicado es: " , descuento)
##Total  de la compra
    totalDescuento= totalCompra-descuento
    print(f"El valor total de la compra con el descuento aplicado al producto {nombreProducto} es de:" , totalDescuento)

if descuentoProducto<0:

    print("Rango de descuento no valido")



    




