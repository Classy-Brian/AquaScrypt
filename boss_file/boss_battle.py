from deck import Deck
import card
from cards.abyssal import angler,jellyfish,kraken
from cards.oceanic import leviathan, manta_ray, shark
from cards.tropical import dolphin,otter, turtle
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
                use_sigil(boss, hidden_upcoming, upcoming_attack, curr_attack, curr_hero, scale)
                sigil = True
            else: 
                print("\nYou can only use one sigil per turn, good luck!")
        else:
            villian_play_card(upcoming_attack, curr_attack, hidden_upcoming)
            display_board(hidden_upcoming, upcoming_attack, curr_attack, curr_hero, scale)
            done = True
    return heroAttack(curr_hero, curr_attack, scale)

def boss_mechanic(boss, upcoming_attack, curr_attack, curr_hero, hidden_upcoming, dmg_mech, scale, bossNum, phase2=False):
    
    if boss._name == "Bubble Bass":
        pause()
        print("Bubble Bass Intro")
        bossNum = 1

        """  dmg_mech is used to keep track of the idx of the card that are bubbled.

            What I am thinking is where there is:
                0: No card, no damage 
                1: There is a card, -1 dmg to card
                2: Contaminated bubble, -2 dmg to card
        """

        """ Adds a bubble to the curr_hero cards. """
        for i, card in enumerate(curr_hero):
            if card is not None:
                temp = "(" + card.name + ")"
                card.name = temp
                if phase2 == False:
                    dmg_mech[i] = 1
                    print("HAHAHAHAHAAAA....... I trapped your cards in my NASTY BUBBLE!")
                    print("AIN'T NOTHIN YOU CAN DO ABOUT IT!")
                else:
                    dmg_mech[i] = 2
                    print("Ooooooohhh alright ... NOW YOU ARE STARTING TO PISS ME OFF!")
                    print("Have a taste of my CONTAMINATED BUBBLE!")
            else:
                dmg_mech[i] = 0
        
        return dmg_mech, bossNum
    
    elif boss._name == "Scuba Diver":
        pause()
        print("Scuba Diver Intro")
        bossNum = 2

        """  dmg_mech 
                0: No card, no damage 
                1: Kill off all curr_hero cards
                2: Kill off all curr_hero cards ... again (Maybe put a temp barrier where the platyer can't place any card in it for a round)
        """

        for i, card in enumerate(curr_hero):
            if card is not None:
                if phase2 == False:
                    dmg_mech[i] = 1
                    print("I have speared all your fishes! What chu gonna do bout it???")
                else:
                    dmg_mech[i] = 2
                    print("Aight aight, how about this!")
        
        return dmg_mech, bossNum

    elif boss._name == "Seraphina, Empress of the Abyss":
        pause()
        print("Mermaid Intro")
        bossNum = 3

        """  dmg_mech 
                0: No card, no damage 
                0: No card, no damage 
                0: No card, no damage 
        """

        myShrimp = shrimp.Shrimp()
        for i, card in enumerate(curr_attack):
            if phase2 == False:
                myShrimp._power = 1
                myShrimp._max_hp = 2
                myShrimp._hp = 2
                curr_attack[i] = myShrimp
                
            else:
                myShrimp._power = 1
                myShrimp._max_hp = 1
                myShrimp._hp = 1
                curr_attack[i] = myShrimp
                upcoming_attack[i] = myShrimp
                hidden_upcoming[i] = myShrimp
        
        return dmg_mech, bossNum

def death_messages(curr_attack):
    last_attack_card = None
    for card in curr_attack:
        if card is not None:
            last_attack_card = card
    
    if last_attack_card is not None:
        print(f"{last_attack_card.death_mess()}")
            
def boss_battle(hero, boss):
    print("------------- Boss Battle -------------\n")
    
    shrimp_count = 20
    my_shrimp = shrimp.Shrimp()

    hero_hand = []
    play_deck = copy.deepcopy(hero._deck)
    #play_deck = deck.Deck()
    play_deck.shuffle()

    for _ in range(4):
        hero_hand.append(random_card(play_deck))

    scale = 0
    turn = 0
    hidden_upcoming = [None, None, None, None]
    upcoming_attack = [None, None, None, None]
    curr_attack =     [None, None, None, None]
    curr_hero =       [None, None, None, None] # 2 0 2 0

    active = False
    count = 0  

    dmg_mech = [0,0,0,0] # Index of cards that got inflicted by the mechanic
    bossNum = -1 # Which boss the player is currently dealing with

    print(str(boss))

    while scale > -5 and scale < 10:
        if len(play_deck) -1 < 0:
            scale == -5

        # villian turn 
        if turn == 0:
            
            print("\n---- Boss Turn ----\n")
            if scale >= 3 and scale <=8:
                if active is False:
                    if count != 2:
                        print(boss.power())
                        if count == 0:
                            dmg_mech, bossNum = boss_mechanic(boss, upcoming_attack, curr_attack, curr_hero, hidden_upcoming, dmg_mech, scale, bossNum, False) # mechanic part here // returns an array on indexs on what gets damage
                        else:
                            dmg_mech, bossNum = boss_mechanic(boss, upcoming_attack, curr_attack, curr_hero, hidden_upcoming, dmg_mech, scale, bossNum, True)
                        print(boss.power())
                        print(f"Boss number: {bossNum}")
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

            print(dmg_mech)
            for i, slot in enumerate(dmg_mech):

                # Bubble Bass damage mechanic
                if slot == 1 and bossNum == 1:
                    curr_hero[i].take_damage(1)
                    if curr_hero[i]._hp <= 0:
                        print(f"{curr_hero[i]._name} has suffocated from Bubble Bass's NASTY BUBBLE!")
                        curr_hero[i] = None
                        dmg_mech[i] = 0
                elif slot == 2 and bossNum == 1:
                    curr_hero[i].take_damage(2)
                    if curr_hero[i]._hp <= 0:
                        print(f"{curr_hero[i]._name} has slowly ... painfully ... suffocated from Bubble Bass's CONTAMINATED BUBBLE!")
                        curr_hero[i] = None
                        dmg_mech[i] = 0
                
                # Scuba Diver damage mechanic
                if slot == 1 and bossNum == 2:
                    print(f"{curr_hero[i].name} has been shot by a SPEARGUN!")
                    curr_hero[i] = None
                    dmg_mech[i] = 0
                elif slot == 2 and bossNum == 2:
                    print(f"{curr_hero[i].name} has been shot and impaled! It's lifeless body floats back to the surface...")
                    curr_hero[i] = None
                    dmg_mech[i] = 0
                
                if bossNum == 3:
                    print("An army of shrimps is heading your way! ")
            
            display_board(hidden_upcoming, upcoming_attack, curr_attack, curr_hero, scale)
            
            if scale <= -3:
                print(boss.attack())
                scale = hero_turn(hero_hand, play_deck, shrimp_count, my_shrimp, curr_hero, scale, upcoming_attack, hidden_upcoming, curr_attack,boss, hero)
                pause()
                turn = 0
            
            else:
                scale = hero_turn(hero_hand, play_deck, shrimp_count, my_shrimp, curr_hero, scale, upcoming_attack, hidden_upcoming, curr_attack,boss, hero)
                pause()
                turn = 0

    if scale <= -5:
        clear_terminal()
        delay_print(f"Game Over You Drowned\n")
        death_messages(curr_attack)
        pause()
        choice = check_input.yes_no("Try again? Y/N\n")
        if choice is True:
            boss_battle(hero, boss)

        else:
            exit()
    elif scale >= 10:
        clear_terminal()
        delay_print(f"You have defeated the evil {boss._name}\n You can move forward!")
        pause()
        clear_terminal()