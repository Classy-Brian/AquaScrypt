import deck
import card
from boss_file import boss
from battle import random_card, draw_card, show_hand, display_board, placeCard, use_item, use_sigil, villian_play_card, heroAttack, villian_attack, villian_draw_card
from cards import shrimp
import check_input
from terminal_utils import clear_terminal, pause, delay_print, delay_input, delay
import copy

def boss_turn(boss, upcoming_attack, curr_attack, curr_hero, hidden_upcoming, scale):
    villian_draw_card(boss, upcoming_attack, hidden_upcoming)
    return villian_attack(hidden_upcoming, upcoming_attack, curr_attack, curr_hero, scale) 

def hero_turn(hero_hand, play_deck, shrimp_count, my_shrimp, curr_hero, scale, upcoming_attack, hidden_upcoming, curr_attack,boss, hero):
    """ Draws and sacerfices cards, and attacks villian """
    draw_card(hero_hand, play_deck, shrimp_count, my_shrimp)
    sigil = False 
    done = False
    while not done:
        print("\n1. Look at your cards \n2. Look at board \n3. Place a card down \n4. Use an item \n5. Use Sigil \n6. End turn")
        choice = check_input.range_int("Enter choice: ", 1, 6)
        if choice == 1:
            show_hand(hero_hand)
        elif choice == 2:
            display_board(hidden_upcoming, upcoming_attack, curr_attack, curr_hero, scale)
        elif choice == 3:
            placeCard(hero_hand, curr_hero)
            display_board(hidden_upcoming, upcoming_attack, curr_attack, curr_hero, scale)
        elif choice == 4:
            if len(hero._items) == 0:
                print("\nYou have no items")
            else:
                print("\nWhich item would you like to use?")
                count = 1
                for item in hero._items:
                    print(f"{count}. {item}")
                    count += 1
                valid = False
                while not valid:
                    item_choice = check_input.range_int("Choice: ", 1, count)
                    item_choice -= 1
                    if hero._items[item_choice - 1] is not None:
                        choice_1= check_input.yes_no(f"Are you sure you want to chosse your {hero._items[item_choice - 1]} item?\n")
                        if choice_1 is True:
                            scale = use_item(hero_hand, play_deck, curr_hero, scale, hero._items[item_choice - 1])
                            valid = True
                    else:
                        print("Nothing there! try again")
        elif choice == 5:
            if sigil is False:
                "might need to tweak this"
                use_sigil(boss, hidden_upcoming, upcoming_attack, curr_attack, curr_hero, scale)
                sigil = True
            else: 
                print("\nYou can only use one sigil per turn, good luck!")
        else:
            villian_play_card(upcoming_attack, curr_attack, hidden_upcoming)
            display_board(hidden_upcoming, upcoming_attack, curr_attack, curr_hero, scale)
            done = True
    return heroAttack(curr_hero, curr_attack, scale)

def boss_mechanic(boss, upcoming_attack, curr_attack, curr_hero, hidden_upcoming, scale):
    

    if boss._name == "Bubble Bass":
        print("Bubble Bass")
    
    elif boss._name == "Scuba Diver":
        print("hello")

    elif boss._name == "Mermaid":
        print("hello")

def boss_battle(hero, boss):
    print("------------- Boss Battle -------------\n")
    
    shrimp_count = 20
    my_shrimp = shrimp.Shrimp()

    hero_hand = []
    play_deck = copy.deepcopy(hero._deck)

    play_deck.shuffle()

    for _ in range(4):
        hero_hand.append(random_card(play_deck))
    
    scale = 0
    turn = 0
    hidden_upcoming = [None, None, None, None]
    upcoming_attack = [None, None, None, None]
    curr_attack =     [None, None, None, None]

    # dolhpin = card.Card("Dolphin", 2, 2, 2, "Echolocation", False)
    # Angler = card.Card("Angler", 1, 2, 1, "Bioluminescence", False)
    # Jellyfish = card.Card("Jellyfish", 2, 1, 2, "Swarm", False)
    # Otter = card.Card("Otter", 1, 1, 2, "Swift", False)
    curr_hero =       [None, None, None, None]
    

    # Puts card to upcoming attack first turn 
    # villian_draw_card(villian, upcoming_attack, upcoming_attack)
    active = False
    count = 0  

    print(str(boss))

    while scale > -5 and scale < 10:
        
        
        # villian turn 
        if turn == 0:
            
            print("\n---- Boss Turn ----\n")
            if scale >= 3 and scale <=8:
                if active is False:
                    if count != 2:
                        print(boss.power())
                        boss_mechanic(boss, upcoming_attack, curr_attack, curr_hero, hidden_upcoming, scale) # mechanic part here 
                        print(boss.power())
                        count += 1
                    else:
                        active = True
                        print(boss.attack()) 

                scale = boss_turn(boss, upcoming_attack, curr_attack, curr_hero, hidden_upcoming, scale)
                pause()
                turn = 1

            else:
                scale = boss_turn(boss, upcoming_attack, curr_attack, curr_hero, hidden_upcoming, scale)
                pause()
                turn = 1

        # Hero turn
        else:
            print("\n---- Hero Turn ----\n")
            if scale <= -3:
                print(boss.attack())
                scale = hero_turn(hero_hand, play_deck, shrimp_count, my_shrimp, curr_hero, scale, upcoming_attack, hidden_upcoming, curr_attack,boss, hero)
                pause()
                turn = 0
            
            else:
                scale = hero_turn(hero_hand, play_deck, shrimp_count, my_shrimp, curr_hero, scale, upcoming_attack, hidden_upcoming, curr_attack,boss, hero)
                pause()
                turn = 0






"""
Bubble Bass (Up to change)
- Boss health is doubled than regular villans
- Mechanic starts when scale reaches 3 and 8
- Randomly places 2 bubbles in any slot
- Clear boss playing card
- Player must pop the bubbles if they wish to play on that slot
- If card gets bubbled:
    - puts into deck and to pop up, it must be played back in otherwise each round it loses health
    - ipt traped and cannot do any damage on the board and each round it takes damage, must be popped to continue fighting
    - bubble zombie
    - hallucination 

Scuba Diver / fisherman

Pollution / Mermaid (Ursula from Little Mermaid)

"""