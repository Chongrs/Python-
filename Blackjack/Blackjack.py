import random
from cards import whole_cards

def main():
    
    Player = {
        "Player_1" : [],
        "Player_2" : [],
    }
    
    Cards = {
        "Player_1" : [],
        "Player_2" : [],
        }

    Player_card_value = {
        "Player_1" : None,
        "Player_2" : None,
    }

    key_list = list(whole_cards().keys())
    number_of_cards = len(key_list) - 1

    # FIRST DRAW
    for player in Player: 
        for i in range (2):
            Player[player].append(draw_card(number_of_cards,key_list))
            Cards[player].append(Player[player][i][0])
            Player_card_value[player] = Player[player][0][1] + Player[player][i][1]
            number_of_cards -= 1

    
    print("First Draw")
    for i in Cards:
        print(i, Cards[i], Player_card_value[i])
        show_winner(i, check_winner(Player_card_value[i], i)[0])
        if check_winner(Player_card_value[i], i)[0] == "win":
            break
    
    
    if check_winner(Player_card_value[i], i) == "draw":   # CAN TRY RECURSION
        for player in Player: 
            for i in range (3):
                Player[player].append(draw_card(number_of_cards,key_list))
                Cards[player].append(Player[player][i+2][0])
                Player_card_value[player] = (Player_card_value[player] + Player[player][i+2][1])
                number_of_cards -= 1


                if check_winner(Player_card_value[player], player) == "draw":
                    pass
                else:
                    break
    
    
    print("Second Draw")
    for i in Cards:
        print(i, Cards[i], Player_card_value[i])
        show_winner(i, check_winner(Player_card_value[i], i)[0])
        if check_winner(Player_card_value[i], i)[0] == "win":
            break
        


def draw_card(number_of_cards,key_list):

    card_index = random.randint(0,number_of_cards)
    number_of_cards -= 1
    
    card_drawn = key_list.pop(card_index)

    card_value = whole_cards().pop(card_drawn)
 
    return card_drawn, card_value, number_of_cards


def check_winner(Player_card_value,player):
    if Player_card_value == 21:
        return "win", player
    elif Player_card_value > 21:
        return "lose", player
    else:
        return "draw"
    
def show_winner(player, state):
    if state == "win":
        print(f"{player} wins the game!")
    elif state == "lose":
        print(f"{player} loses the game!")
    


main()