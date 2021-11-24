per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Ввести сумму первичного вклада"))
TKB = int((per_cent['ТКБ']) * (money/100))
CKB = int((per_cent['СКБ']) * (money/100))
BTB = int((per_cent['ВТБ']) * (money/100))
SBER = int((per_cent['СБЕР']) * (money/100))
deposit = [TKB,CKB,BTB,SBER]
print(deposit)
deposit1 = max(deposit)
print('Максимальная сумма, которую вы можете заработать-', deposit1)

