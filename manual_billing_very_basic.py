print('The Smart food')
customer_1 = 'Ali'
items_ali = '1-Chips, 1-Shawarma, 1-Zinger'
bill_1 = 2000

customer_2 = 'Sara'
items_sara = '1-Pasta, 1-Coke, 5-Glass'
bill_2 = 1000

customer_3 = 'Georgia'
items_georgia = '2-Pasta, 3-Zinger, 3-Regular-Coke, 5-Pizza'
bill_3 = 10000

total = bill_1 + bill_2 + bill_3

print('Total Revenue Today')

print(customer_1, bill_1 , items_ali, sep=' ------ ')
print(customer_2, bill_2, items_sara, sep=' ------ ')
print(customer_3, bill_3, items_georgia, sep=' ----  ')
print('_--_+-*/%_--_')
print("Total", total, sep='~~~~~~~~~~~~~~')