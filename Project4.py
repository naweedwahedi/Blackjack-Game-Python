from random import choice as rc
def total_Cards_inHand(cards_inHand):
    ace = cards_inHand.count(11) 
    total = sum(cards_inHand) # To find sum of cards in hand
    if total > 21 and ace > 0:
        while ace > 0 and total > 21:
            total -= 10
            ace -= 1
    return total # return total
totcards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] # lets take suit with following values
player1win = 0 # player1 win counter
player2win = 0 # player2 win counter
while True: # player 1 turn
    play1 = [] # empty hand
    play1.append(rc(totcards)) # draw 2 cards for the player 1 to start
    play1.append(rc(totcards))
    player1bust = False # player 1 busted flag
    while True:
        # loop for the player's play ...
        totalp1 = total_Cards_inHand(play1) # counting sum of values in the hand
        print ("The player 1 has these cards %s with a total value of %d" % (play1, totalp1)) # printing that value
        if totalp1 > 21: # if value >21
            print ("--> The player 1 is busted!") # lost
            player1bust = True
            break
        elif totalp1 == 21: # if equals to 21
            print ("\a BLACKJACK!!!") # wins
            break
        else: # else
            hors = input("Hit or Stand/Done (h or s): ").lower() # ask for another card
            if 'h' in hors:
                play1.append(rc(totcards)) # append it to our suit
            else:
                break # or break
    while True: # player 2 turn
        play2 = []
        play2.append(rc(totcards)) # draw 2 cards for the player 2 to start
        play2.append(rc(totcards))
        player2bust = False # player 2 busted flag
        totalp2 = total_Cards_inHand(play2)
        print ("The player 2 has these cards %s with a total value of %d" % (play2, totalp2))
        if totalp2 > 21: # same conditions for player 2 as for player 1
            print ("--> The player 2 is busted!")
            player2bust = True
            break
        elif totalp2 == 21:
            print ("\a BLACKJACK!!!")
            break
        else:
            hors = input("Hit or Stand/Done (h or s): ").lower()
            if 'h' in hors:
                play2.append(rc(totcards))
            else:
                break
    
    if totalp2 > 21: # now figure out who won ...
        player2bust = True # if player 2 is burst
        if player1bust == False:
            print ("The player 1 wins!") # then player 1 wins
            player1win += 1 # increase player 1 wins
    elif totalp2 > totalp1: # plalyer 2 score > player 1 score
        print ("The player 2 wins!") # player 2 wins
        player2win += 1 # increase player 2 wins
    elif totalp1 == totalp2: # if scores are equal
        print ("It's a draw!") # its draw
    elif totalp1 > totalp2: # if player1 has greater than player 2 score
        if player2bust == False:
            print ("The player 1 wins!") # player 1 wins
            player1win += 1 # increase the player 1 wins
        elif player2bust == False: # else
            print ("The player 2 wins!") # plater 2 wins
            player2win += 1 # increase player 2 wins
            break
    print
    print ("Wins, player 1 = %d player 2 = %d" % (player1win, player2win))# printing the wins of player 1 and player 2
    exit = input("Press Enter (q to quit): ").lower() # if wants to play again or not
    if 'q' in exit: # if no
        break
    print
print
print ("Thanks for playing blackjack!") # end message