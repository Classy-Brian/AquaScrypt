import deck
import card
from boss_file import boss
from battle import random_card, draw_card, show_hand, display_board, placeCard, use_item, use_sigil, villian_play_card, heroAttack
from cards import shrimp
import check_input
from terminal_utils import clear_terminal, pause, delay_print, delay_input, delay

def boss_turn(boss, upcoming_attack, curr_attack, curr_hero, hidden_upcoming, scale):
    print("hello")

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

def boss_battle(hero, boss):
    print("------------- Boss Battle -------------")
    
    shrimp_count = 20
    my_shrimp = shrimp.Shrimp()

    hero_hand = []
    play_deck = hero._deck 
    play_deck.shuffle()
    for _ in range(4):
        hero_hand.append(random_card(play_deck))

    boss._deck.shuffle()
    
    scale = 0
    turn = 0
    hidden_upcoming = [None, None, None, None]
    upcoming_attack = [None, None, None, None]
    curr_attack =     [None, None, None, None]

    dolhpin = card.Card("Dolphin", 2, 2, 2, "Echolocation", False)
    Angler = card.Card("Angler", 1, 2, 1, "Bioluminescence", False)
    Jellyfish = card.Card("Jellyfish", 2, 1, 2, "Swarm", False)
    Otter = card.Card("Otter", 1, 1, 2, "Swift", False)
    curr_hero =       [None, None, None, None]
    

    # Puts card to upcoming attack first turn 
    # villian_draw_card(villian, upcoming_attack, upcoming_attack)

    while scale > -5 and scale < 5:
        
        # villian turn
        if turn == 0:
            print("\n---- Villain Turn ----\n")
            scale = boss_turn(boss, upcoming_attack, curr_attack, curr_hero, hidden_upcoming, scale)
            pause()
            turn = 1
        # Hero turn
        else:
            print("\n---- Hero Turn ----\n")
            scale = hero_turn(hero_hand, play_deck, shrimp_count, my_shrimp, curr_hero, scale, upcoming_attack, hidden_upcoming, curr_attack,boss, hero)
            pause()
            turn = 0