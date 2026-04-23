items_1 = input('Enter name of the item: \n')
items_1_Quantity = int(input('Please enter quantity of ' + items_1 + ': \n'))

items_2 = input('Enter name of the item: \n')
items_2_Quantity = int(input('Please enter quantity of ' + items_2 + ': \n'))

items_3 = input('Enter name of the item: \n')
items_3_Quantity = int(input('Please enter quantity of ' + items_3 + ': \n'))

user_wants_to = int(input('Enter "1" if you want to make a sale, \n "2" to check stock of all items \n "3" to check items which are low on stock \n "4" to add stock to axisting items: \n'))

if user_wants_to == 1 :
    print('Select items 1 for ', items_1, '2 for ', items_2, '3 for ', items_3, '\n' )

    user_sells = int(input('Enter you selected one: '))
    if user_sells ==  1:
        print(items_1, 'has in stock ', items_1_Quantity, 'kg')
        how_much = int(input('Enter quantity to sell \n'))
        items_1_Quantity = items_1_Quantity - how_much
        print(items_1, 'has left in stock ', items_1_Quantity, 'kg')

    elif user_sells ==  2:
        print(items_2, 'has in stock ', items_2_Quantity, 'kg')
        how_much = int(input('Enter quantity to sell \n'))
        items_2_Quantity = items_2_Quantity - how_much
        print(items_2, 'has left in stock ', items_2_Quantity, 'kg')

    elif user_sells ==  3:
        print(items_3, 'has in stock ', items_3_Quantity, 'kg')
        how_much = int(input('Enter quantity to sell \n'))
        items_3_Quantity = items_3_Quantity - how_much
        print(items_3, 'has left in stock ', items_3_Quantity, 'kg')


elif user_wants_to == 2:
    print(items_1, 'has left in stock ', items_1_Quantity, 'kg')
    print(items_2, 'has left in stock ', items_2_Quantity, 'kg')
    print(items_3, 'has left in stock ', items_3_Quantity, 'kg')


elif user_wants_to == 3:
    if items_1_Quantity <= 3:
        print(items_1,' has left only ', items_1_Quantity, 'kg')

    if items_2_Quantity <= 3:
        print(items_2,' has left only ', items_2_Quantity, 'kg')

    if items_3_Quantity <= 3:
        print(items_3,' has left only ', items_3_Quantity, 'kg')



    


    else:
        print('All tiems are above 3kg ')


elif user_wants_to == 4:
    print('Select items 1 for ', items_1, '2 for ', items_2, '3 for ', items_3 )
    user_icreases = int(input('Enter you selected one: '))

    if user_icreases ==  1:
        print(items_1, 'has in stock ', items_1_Quantity, 'kg')
        how_much = int(input('Enter quantity to add \n'))
        items_1_Quantity = items_1_Quantity + how_much
        print(items_1, 'has left in stock ', items_1_Quantity, 'kg')

    elif user_icreases ==  2:
        print(items_2, 'has in stock ', items_2_Quantity, 'kg')
        how_much = int(input('Enter quantity to add \n'))
        items_2_Quantity = items_2_Quantity + how_much
        print(items_2, 'has left in stock ', items_2_Quantity, 'kg')

    elif user_icreases ==  3:
        print(items_3, 'has in stock ', items_3_Quantity, 'kg')
        how_much = int(input('Enter quantity to add \n'))
        items_3_Quantity = items_3_Quantity + how_much
        print(items_3, 'has left in stock ', items_3_Quantity, 'kg')
    
    
    









