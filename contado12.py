numero = abs(int(input("Ingrese un número entero: ")))
contador = 0

if numero == 0:
    contador = 1
else:
    while numero > 0:
        contador += 1
        numero //= 10

print(f"El número tiene {contador} dígito(s)")