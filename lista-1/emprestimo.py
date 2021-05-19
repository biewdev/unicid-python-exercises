home = float(input("Qual o valor da casa? "))
print("Valor da casa:", home)

salary = float(input("Qual o valor do salário? "))
print("Salario:", salary)

years = int(input("Qual a quantidade de anos para pagar? "))
print("Anos a pagar:", years)

limit = salary / 100 * 30
time = years * 12
render = home / time

if render > limit:
    print("Empréstimo Negado")
if render <= limit:
    print("Empréstimo Aprovado")
