import random
playerIn = True
dealerIn = True

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        'Jack', 'Queen', 'King', 'Ace', 'Jack', 'Queen', 'King', 'Ace', 'Jack', 'Queen', 'King', 'Ace', 'Jack', 'Queen', 'King', 'Ace', ]
playerhand = []
dealerhand = []

def dealcard(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

def total(turn):
    total = 0
    Ace_11 = 0
    # face = ['King', 'Jack', 'Queen']
    for card in turn:
        if card in range(11):
            total += card
        elif card in ['King', 'Jack', 'Queen']:
            total += 10
        else:
            total += 11
            Ace_11 += 1
    while Ace_11 and total > 21:
        total -= 10
        Ace_11 -= 1
    return total

def revealdealerhand():
    if len(dealerhand) == 2:
        return dealerhand[0]
    elif len(dealerhand) > 2:
        return dealerhand[0], dealerhand[1]


for c in range(2):
    dealcard(dealerhand)
    dealcard(playerhand)

while playerIn or dealerIn:
    print('Dealer had', revealdealerhand())
    print('You have', playerhand, 'for a total of', total(playerhand))
    if playerIn:
        stayORhit = input('Choose: 1 == Stay, 2 == Hit ')
    if total(dealerhand) > 16:
        dealerIn = False
    else:
        dealcard(dealerhand)
    if stayORhit == '1':
        playerIn = False
    else:
        dealcard(playerhand)
    if total(playerhand) >= 21:
        break
    elif total(dealerhand) >= 21:
        break

if total(playerhand) == 21:
    print('You have', playerhand, 'for a total of', total(playerhand), dealerhand, 'for a total of', total(dealerhand))
    print("BlackJack! You win! Congarts.")
elif total(dealerhand) == 21:
    print('You have', playerhand, 'for a total of', total(playerhand), dealerhand, 'for a total of', total(dealerhand))
    print('BlackJack! Dealer wins!')
elif total(playerhand) > 21:
    print('You have', playerhand, 'for a total of', total(playerhand), dealerhand, 'for a total of', total(dealerhand))
    print('You bust! dealer wins!')
elif total(dealerhand) > 21:
    print('You have', playerhand, 'for a total of', total(playerhand), dealerhand, 'for a total of', total(dealerhand))
    print('Dealer busts! You win!')
elif 21 - total(dealerhand) > 21 - total(playerhand):
    print('You have', playerhand, 'for a total of', total(playerhand), dealerhand, 'for a total of', total(dealerhand))
    print("Dealer busts! You win!")
elif 21 - total(dealerhand) < 21 - total(playerhand):
    print('You have', playerhand, 'for a total of', total(playerhand), dealerhand, 'for a total of', total(dealerhand))
    print('You bust! Dealer won!')
else:
    print('You have', playerhand, 'for a total of', total(playerhand), dealerhand, 'for a total of', total(dealerhand))
    print('It is a tie!')


