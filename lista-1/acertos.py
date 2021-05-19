points = 0

answer_one = input("Resposta da primeira questão: ")
if answer_one.lower() == "B".lower():
    points += 1

answer_two = input("Resposta da segunda questão: ")
if answer_two.lower() == "A".lower():
    points += 1

answer_three = input("Resposta da terceira questão: ")
if answer_three.lower() == "D".lower():
    points += 1

print("Total de pontos:", points)
