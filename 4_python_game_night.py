import random


#   Create a game where a player has a list of items
#   They have to guess which item in the list was selected. 
#   Use random.choice() to select the item and take the user's guess via input.
#   Provide feedback on whether they guessed correctly or not keep them playing until they guess correctly.

card = input('pick a card type: ')
type = ('Hearts', 'Spade', 'Clubs', 'Diamond ')

while True:
    my_choice = card
    dealer = random.choice(type)
    print('Dealer Chose:', dealer)
    win = input('Did You Beat the House? ')
    if win == 'yes':
        print('The House Always Wins, Nice Try')
        dealer = random.choice(type)
        break
    if win == 'no':
        print('Play Again!')
        dealer = random.choice(type)