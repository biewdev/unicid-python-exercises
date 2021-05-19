number = int(input("Digite o número: "))
inverted = int(str(number)[::-1])
if number == inverted:
    print("É palíndromo")
else:
    print("Não é palíndromo")
