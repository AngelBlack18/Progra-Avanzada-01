### EJERCICIO (Funciones)
# Somos una caja registradora...
# El cliente nos paga con "x" cantidad de dinero, y compra un articulo de "y" precio
# Cuanto nos sobra? (imprimir)
# Podemos tener varios clientes (tenemos que usar un ciclo)

pago = float(input('Ingrese la cantidad de dinero: '))
precio = float(input('Ingrese el precio del articulo a comprar: '))

def caja_registradora(pago, precio):
    resultado = pago - precio   # hacer los calculos necesarios...
    return print("Su cambio es->",resultado)

caja_registradora(pago, precio)