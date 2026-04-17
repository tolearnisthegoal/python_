item = 'TO sell:   Rare Diamond'
amount = 100
first = 'Ali '
amount_1 = 300

second = 'Ahmad '
amount_2 = 500

third = 'Ali '
amount_3 = 800

filler_1 = '('
filler_2 = ')'

print(item)

print('Bid starts at: ', end=' ')
print(amount, '\n')

print(first, '(',amount_1, ') ', second, '(',amount_2, ') ', third, '(',amount_3, ')', sep='')

print()


print('Winner: ', third, '@', amount_3)
