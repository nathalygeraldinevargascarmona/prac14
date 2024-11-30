print ("HERNANDEZ PALFOX Y VARGAS CARMONA")
def generar_fibonacci(cantidad):
    numeros_fib = [0, 1]
    for i in range(2, cantidad):
        siguiente_numero = numeros_fib[i - 1] + numeros_fib[i - 2]
        numeros_fib.append(siguiente_numero)
    return numeros_fib
cantidad_numeros = int(input("Cuantos numeros de la secuencia de Fibonacci te gustaria ver "))
if cantidad_numeros <= 0:
    print("ingresa un numero mayor que 0.")
else:
    secuencia_fib = generar_fibonacci(cantidad_numeros)
    print("Secuencia de Fibonacci:")
    print(secuencia_fib)