shop_Name = input('Enter your shop name \n')
s_N = shop_Name.strip().capitalize().center(10)


customer_Name = input('Enter Customer name \n')
c_N = customer_Name.strip().capitalize().center(10)


item_Name = input('Enter what you sold  \n')
i_N = item_Name.strip().capitalize().center(10)


price = int(input('Enter Price \n'))

print('========== ', s_N, " ==========")
print('Customer Name: ',c_N)
print('------------------------------------')
print('Item Sold: ',i_N)
print('Price is: ',price)
print('------------------------------------')
print('Total: ', price)
print('====================================')
