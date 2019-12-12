account = 400
interest = float(input('Welchen Zinssatz' + ' möchtest du haben ? '))

print("Kontostand: ")
print(account)
print("Kontostand + Zinsen ")
print('neuer Kontostand: ' + str(account + account * (interest/100)))
