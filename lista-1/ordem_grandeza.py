n = int(input("Digite o valor do numero: "))
if n >= 0 and n < 100:
    print(n, "entre 0 e 100")
elif n >= 100 and n < 1000:
    print(n, "entre 100 e 1000")
elif n >= 1000:
    print(n, "maior ou igual a 1000")
elif n < 0:
    print(n, "menor que zero")
