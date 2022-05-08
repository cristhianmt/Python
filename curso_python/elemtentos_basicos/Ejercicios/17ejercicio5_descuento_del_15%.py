"""
En una tienda ofrece el descuento del 15% sobre el total de la compra  y un cliente
desea saber cuanto debera pagar finalmente por su compra
"""

producto=str(input("Digite su producto: "))
precio=float(input("Digite el precio sin descuento: "))

descuento= precio*0.15
preciofinal=precio-descuento
print(f"El precio final de {producto} es de {preciofinal:2f}")