price = float(input("Digite o valor: "))
banknotes = [100, 50, 20, 10, 4, 1]
bankcoins = [0.50, 0.10, 0.05, 0.02, 0.01]
minprice = 0.01
trade = float(price)

if price >= minprice:
    while trade > 0:
        for note in banknotes:
            if trade >= note:
                notes = int(trade / note)
                rest = trade - (notes * note)
                trade = float("{:.2f}".format(rest))
                print(notes, "nota(s) de R$", note)
        for coin in bankcoins:
            if trade >= coin:
                coins = int(trade / coin)
                rest = trade - (coins * coin)
                trade = float("{:.2f}".format(rest))
                print(coins, "moeda(s) de", coin, "centavo(s)")
else:
    print("Não aceitamos valores abaixo de", minprice, "centavo(s)")
