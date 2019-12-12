tv_available = True
bank_balance = 400.10

preis = float(input('Wieviel Geld möchtest du Ausgeben ? '))
bank_balance = bank_balance - preis

if bank_balance > 0:
    print('Einkauf ist ok')
else:
    print('du bist im Minus')
