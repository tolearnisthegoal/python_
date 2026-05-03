import art
print(art.logo)

bidding = True
bid_data = {}

while bidding:
    # TODO-1: Ask the user for input
    name = input('What is you name?: ')
    price = float(input('What is your bid?: $'))
    # TODO-2: Save data into dictionary {name: price}

    bid_data[name] = price

    # TODO-3: Whether if new bids need to be added
    more_bids = input('\nAre there any other bidders? Type (y/n):\n ')
    if more_bids == 'n':
        bidding = False
# TODO-4: Compare bids in dictionary
compare = 0
name_in_dic = ''
for key in bid_data:
    if bid_data[key] > compare:
        compare = bid_data[key]
        name_in_dic = key

print(f'The winner is {name_in_dic} with a bid of ${compare}')








