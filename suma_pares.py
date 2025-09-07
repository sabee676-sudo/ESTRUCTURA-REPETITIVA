n= int(input("Ingresa un número: "))


while i <= n:
    if i % 2 == 0:
        suma_pares += i
    else:
        suma_impares += i
    i += 1

print(f"Suma de pares: {suma_pares}")
print(f"Suma de impares: {suma_impares}")