print('The Smart food')


item_chips = 'Chips'
item_chips_p = 150

item_shawarma = 'Shawarma'
item_shawarma_p = 250

item_zinger = 'Zinger'
item_zinger_p = 450

item_coke = 'Coke'
item_coke_p = 750

item_pasta = 'Pasta'
item_pasta_p = 900


print('-----------------')
customer_1 = 'Ali'
print(customer_1)
print('---')
print(1, item_chips, 1, item_shawarma, 1, item_zinger)

bill_1 = item_chips_p + item_shawarma_p + item_zinger_p
print(bill_1)


print('-----------------')
customer_2 = 'Sara'
print(customer_2)
print('---')
print(3, item_pasta, 5, item_zinger)
bill_2 = (3*item_pasta_p) + (5 * item_zinger_p)
print(bill_2)


print('-----------------')
customer_3 = 'Georgia'
print(customer_3)
print('---')
print(5, item_pasta, 5, item_coke)
bill_3 = (5* item_pasta_p) + (5 * item_coke_p)
print(bill_3)

print('--!+-*/%---')

print('-----------------')

print('Total Revenue Today')

total_revenue = bill_1 + bill_2 + bill_3

print(total_revenue)

