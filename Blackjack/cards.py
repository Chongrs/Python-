def whole_cards():
    
    cards = {}
    card_type = ["A", "B", "C", "D"]

    for card_type_i in card_type :
        
        for card_value in range(14) :
            cards[card_type_i + str(card_value)] = card_value
            if card_value == 11 :
                del cards[card_type_i + str(card_value)]
                cards[card_type_i + "J"] = 10
                
            if card_value == 12 :
                del cards[card_type_i + str(card_value)]
                cards[card_type_i + "Q"] = 10
                
            if card_value == 13 :
                del cards[card_type_i + str(card_value)]
                cards[card_type_i + "K"] = 10
            

    del cards["A0"], cards["B0"], cards["C0"], cards["D0"]
    
    return cards
    
whole_cards()