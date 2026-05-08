import random

art_1 = r''' _  _  __  ___  _  _  ____  ____    __     __   _  _  ____  ____ 
/ )( \(  )/ __)/ )( \(  __)(  _ \  (  )   /  \ / )( \(  __)(  _ \
) __ ( )(( (_ \) __ ( ) _)  )   /  / (_/\(  O )\ /\ / ) _)  )   /
\_)(_/(__)\___/\_)(_/(____)(__\_)  \____/ \__/ (_/\_)(____)(__\_)'''

art_2 = r''' _  _  ____ 
/ )( \/ ___)
\ \/ /\___ \
 \__/ (____/'''

print(art_1)
players_1 = {
    'John posts on a small gamer page': 200,          # small gamer page
    'Michael is a fitness coach': 600,       # fitness coach
    'David is a tech reviewer': 1500,        # tech reviewer
    'James is a travel blogger': 3200,        # travel blogger
    'Robert is a student influencer': 800,        # student influencer
    'William is a YouTuber': 5400,      # YouTuber
    'Daniel is a photographer': 1200,       # photographer
    'Matthew cricket fan page': 2500,      # cricket fan page
    'Joseph is a streamer': 4100,       # streamer
    'Andrew posts on meme page': 900         # meme page
}

players_2 = {
    'Ethan is a tech influencer': 6000,        # tech influencer
    'Liam is a fashion creator': 9000,         # fashion creator
    'Noah is a lifestyle blogger': 7500,         # lifestyle blogger
    'Oliver is a TikTok creator': 11000,      # TikTok creator
    'Lucas is a travel vlogger': 6800,        # travel vlogger
    'Henry runs his own celebrity page': 13000,       # celebrity page
    'Alexander is a fitness influencer': 5000,    # fitness influencer
    'Benjamin is a gaming streamer': 8200,     # gaming streamer
    'Sebastian is a dancer': 9500,    # dancer
    'Jack runs a entertainment page': 10000         # entertainment page
}

choice_1 = random.choice(list(players_1.keys()))
choice_2 = random.choice(list(players_2.keys()))

gamePlay = True
count = 0
while gamePlay:

    print('Guess who has more followers on insta:) ')
    print(f'First is {choice_1}')
    print(art_2)
    print(f'Second is {choice_2}')

    guess = input('Who has more followers? Type \'A\' or \'B\': ').lower()

    if guess == 'a' and players_1[choice_1] > players_2[choice_2]:
        print('Correct!')
        count += 1

    elif guess == 'b' and  players_2[choice_2] > players_1[choice_1]:
        print('Correct!')
        count += 1

    else:
        print('Wrong!')
        gamePlay = False
        break


print(f'You were right {count} times')