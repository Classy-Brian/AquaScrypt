import random
import card 
import copy 
from cards import shrimp
import check_input
from terminal_utils import clear_terminal, pause, delay_print
#from cards.abyssal import angler,jellyfish,kraken <- Test
#from cards.oceanic import leviathan, manta_ray, shark <- Test
#from cards.tropical import dolphin,otter, turtle

def choose_card(text, deck, return_index=False):
    if all(card is None for card in deck):
        return None
    else:
        print(text)
        counter = 1 
        for card in deck:
            print(f"{counter}. {card}")
            print()
            counter += 1

        valid = False
        while not valid:
            choice = check_input.range_int("Enter choice: ", 1, counter - 1)
            

            if deck[choice - 1] is not None:
                choice_2= check_input.yes_no(f"Are you sure you want to choose your {deck[choice - 1].name}?\n")
                if choice_2 == True:
                    if return_index:                 
                        return deck[choice - 1], choice - 1
                    else:
                        return deck[choice - 1]
            else:
                print("There's no card there, choose again. ")

def random_card(deck):
    """ From a deck of cards, pick a random card """
    if len(deck) <= 0:
        print("You have nothing left.")
        return None
    cardNum = random.randint(0, len(deck) - 1)
    card = deck.remove_card(cardNum)
    return card 

def show_hand(hand):
    """ Display current hand """
    print("\n~~~ Current Hand ~~~")
    for card in hand:
        print(card)
        print()

    print("~~~~~~~~~~~~~~~~~~~~\n")

def death_messages(curr_attack):
    last_attack_card = None
    for card in curr_attack:
        if card is not None:
            last_attack_card = card
    
    if last_attack_card is not None:
        print(f"{last_attack_card.death_mess()}")

def display_board(hidden_upcoming, upcoming_attack, curr_attack, curr_hero, scale):
    """ hows current board """
    print(f"\nScale: {scale}")
    print("~~~~~~~~ The Board ~~~~~~~~")

    #Delete once done test
    #for index, card in enumerate(hidden_upcoming):
    #    if card is None:
    #        print("None", end=" ")
    #    else:
    #        print(card.name, end=" ")
    #print("-> Hidden attack")
    #print()

    for index, card in enumerate(upcoming_attack):
        if card is None:
            print("None", end=" ")
        else:
            print(card.name, end=" ")
    print("-> Upcoming attack")
    print()

    for index, card in enumerate(curr_attack):
        if card is None:
            print("None", end=" ")
        else:
            print(card.name, end=" ")
    print("-> Current attack")
    print()        
    
    for index, card in enumerate(curr_hero):
        if card is None:
            print("None", end=" ")
        else:
            print(card.name, end=" ")
    print("-> Current hero")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

def villian_draw_card(villian, upcoming_attack, hidden_upcoming):
    """ Randomly add cards to upcoming_attack and hidden_upcoming """
    for index, card in enumerate(hidden_upcoming):
        if random.randint(0, 1) == 1 and hidden_upcoming[index] is None:  
            hidden_upcoming[index] = villian._deck.draw_card()

def villian_play_card(upcoming_attack, curr_attack, hidden_upcoming):
    """ Pushes it to curr_attack"""
    for index in range(len(upcoming_attack)):
        if upcoming_attack[index] is not None and curr_attack[index] is None:
            curr_attack[index] = upcoming_attack[index]
            if upcoming_attack[index] is not None:
                upcoming_attack[index] = None
    
    for index in range(len(hidden_upcoming)):
        if hidden_upcoming[index] is not None and upcoming_attack[index] is None:
            upcoming_attack[index] = hidden_upcoming[index]
            if hidden_upcoming[index] is not None:
                hidden_upcoming[index] = None

def villian_attack(hidden_upcoming, upcoming_attack, curr_attack, curr_hero, scale):
    """ attacks hero """
    for index, card in enumerate(curr_attack):
        if card is not None:
            if curr_hero[index] is None:
                scale -= card.power
                print(f"The villian's {card.name} dealt {card.power} damage to you ")
            else:
                if curr_hero[index].barrier == False:
                    curr_hero[index].take_damage(curr_attack[index].power)
                    print("The villian's " + str(curr_attack[index].name) + " dealt " + str(curr_attack[index].power) + " damage to your " + str(curr_hero[index].name))
                    if curr_hero[index].hp == 0:
                        print(f"villian {card.name} has slayed your {curr_hero[index].name}")
                        curr_hero[index] = None
                else:
                    if curr_hero[index].sigil != "Swift":
                        print(f"Your {curr_hero[index].name} has a barrier, and villian {str(curr_attack[index].name)} dealt 0 damage")
                        print(f"Your {curr_hero[index].name} barrier broke")
                        curr_hero[index].barrier = False 
                    else:
                        print(f"Your {curr_hero[index].name} has avoid villian {curr_attack[index].name} attack")
                        curr_hero[index].barrier = False
    display_board(hidden_upcoming, upcoming_attack, curr_attack, curr_hero, scale)
    return scale 

def villian_turn(villian, upcoming_attack, curr_attack, curr_hero, hidden_upcoming, scale):
    """ Pushes it to curr_attack and attacks hero """
    villian_draw_card(villian, upcoming_attack, hidden_upcoming)
    return villian_attack(hidden_upcoming, upcoming_attack, curr_attack, curr_hero, scale) 
 
def hero_turn(hero_hand, play_deck, shrimp_count, my_shrimp, curr_hero, scale, upcoming_attack, hidden_upcoming, curr_attack,villian, hero):
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
                use_sigil(villian, hidden_upcoming, upcoming_attack, curr_attack, curr_hero, scale)
                sigil = True
            else: 
                print("\nYou can only use one sigil per turn, good luck!")
        else:
            villian_play_card(upcoming_attack, curr_attack, hidden_upcoming)
            display_board(hidden_upcoming, upcoming_attack, curr_attack, curr_hero, scale)
            done = True
    return heroAttack(curr_hero, curr_attack, scale)

def draw_card(hero_hand, play_deck, shrimp_count, my_shrimp):
    """ User chooses a card of shrimp """
    print("1. Draw from deck \n2. Draw a shrimp")
    choice = check_input.range_int("Enter choice: ", 1, 2)
    if choice == 1:
        new_card = random_card(play_deck)
        hero_hand.append(new_card)
        print(f"\nYou drew a {new_card.name}.")
    elif choice == 2:
        if shrimp_count > 0:
            hero_hand.append(my_shrimp)
            print("\nYou drew a shrimp.")
            shrimp_count -= 1

def placeCard(hero_hand, curr_hero):
    """ Place and sacerfice cards """

    done_choosing = False
    has_enough = 0
    picked_card = None
    while not done_choosing:
        picked_card, index = choose_card("\nChoose a card from your hand", hero_hand, return_index=True)
        if picked_card.cost > 0: 
            for card in curr_hero:
                if card is not None:
                    has_enough += 1
        if has_enough >= picked_card.cost:
            hero_hand[index] = None
            done_choosing = True
        else:
            print("This card requires more creatures to sacerfice then what you currently have on the board.\n")
            has_enough = 0

            choice = check_input.yes_no("Do you want to go back to your turn? (y/n):\n")
            if choice is True:
                return
            

    curr_sac = 0
    if curr_sac < picked_card.cost:
        print(f"\nThis card needs {picked_card.cost} sacerfices. Choose wisely.")
        while curr_sac < picked_card.cost:
            print("Which card would you like to sacerfice?")
            choice_card, index = choose_card("", curr_hero, return_index=True)
            if choice_card.name == "Boulder":
                print("You cannot sacerfice a boulder ... dummy")
            else:
                curr_hero[index] = None
                curr_sac += 1
                print(f"You have sacerficed {choice_card.name} sacerfices: {curr_sac}/{picked_card.cost}")

    card_place = False
    while not card_place:
        print("Where would you like to place the card? Slot 1, 2, 3, or 4")
        choice = check_input.range_int("Enter choice: ", 1, 4)
        if curr_hero[choice - 1] is None:
            curr_hero[choice - 1] = picked_card
            card_place = True
        else:
            print("There is already a card in that slot, pick somewhere else.")

def heroAttack(curr_hero, curr_attack, scale):
    for index, card in enumerate(curr_hero):
        if card is not None:
            if curr_attack[index] is None:
                scale += card.power
                print(f"Your {card.name} have done {card.power} to the villian!")
            else:
                print(card.attack(curr_attack[index]))
                if curr_attack[index].hp == 0:
                    print(f"Your {card.name} has slayed villian {curr_attack[index].name} ")
                    curr_attack[index] = None 
        else:
            print(f"No cards placed in slot {index + 1}")
    return scale

def use_item(hero_hand, play_deck, curr_hero, scale, item):
    
    if item == "Dagger":
        scale += 1 
        print("Scale is now ", scale)
    elif item == "Boulder":
        boulder = card.Card("Boulder", 0, 0, 5, None, False)
        hero_hand.append(boulder)
    elif item == "Shrimp Bottle":
        shrimp = card.Card("Shrimp", 0, 0, 0, None, False)
        hero_hand.append(shrimp)
    else:
        print("Item is not used")
    return scale

def use_sigil(villian, hidden_upcoming, upcoming_attack, curr_attack, curr_hero, scale): 
    end_sigil = False
    enhanced_cards = set()
    while not end_sigil:
        print("Which card do you want to use Sigil? Slot 1, 2, 3, or 4")
        choice = check_input.range_int("Enter choice: ", 1, 4)
        if curr_hero[choice - 1] is not None:
            print(f"\n{curr_hero[choice - 1].desc()}")
            if len(curr_hero[choice - 1].sigil) > 1:
                sigil_choice = check_input.range_int(f"Choose a sigil to use {(curr_hero[choice - 1].sigil)}: ", 1, len(curr_hero[choice - 1].sigil))
                selected_sigil = curr_hero[choice - 1].sigil[sigil_choice - 1]
            else:
                selected_sigil = curr_hero[choice - 1].sigil[0]       
            choice_2= check_input.yes_no(f"Are you sure you want to use {curr_hero[choice - 1].name} sigil?\n")
            if choice_2 == True:
                if selected_sigil == "Bioluminescence":
                    for index, card in enumerate(curr_hero):
                        if curr_hero[index] is not None:
                            if curr_hero[index].name in ["Angler", "Jellyfish", "Kraken"] and curr_hero[index].name not in enhanced_cards:
                                curr_hero[index].power += 1
                                curr_hero[index].hp += 1
                                enhanced_cards.add(curr_hero[index].name)
                    end_sigil = True
                    print(f"\n{curr_hero[choice - 1].name} use Bioluminescence and enhances its self, and other abyssal fish cards!")

                elif selected_sigil == "Swarm":
                    clone_limit = 0
                    card_copies = curr_hero[choice - 1]
                    for index, card in enumerate(curr_hero):
                        if curr_hero[index] is None and clone_limit < 2:
                            clone = copy.copy(card_copies)
                            curr_hero[index] = clone
                            clone_limit +=1 
                    print(f"\n{curr_hero[choice - 1].name} uses Swarm and summons additional copies of itself!")
                    end_sigil = True

                elif selected_sigil == "Frenzy":
                    if curr_hero[choice - 1].hp is not None and curr_hero[choice - 1].hp < (curr_hero[choice - 1].max_hp //2):
                        curr_hero[choice - 1].power *= 2
                        print(f"\n{curr_hero[choice - 1].name} use Frenzy and now will deals double damage!")
                        end_sigil = True 
                    else: 
                        print(f"\n{curr_hero[choice - 1].name} is not low yet, and cannot use Frenzy")

                elif selected_sigil == "Barrier":
                    if not curr_hero[choice - 1].barrier:
                        print(f"\n{curr_hero[choice - 1].name} use Barrier and will blocks the next attack!")
                        curr_hero[choice - 1].barrier = True
                        end_sigil = True
                    else:
                        print(f"\n{curr_hero[choice - 1].name} already has a Barrier active.")

                elif selected_sigil == "Echolocation":
                    print(f"\n{curr_hero[choice - 1].name} use Echolocation and see upcoming attack!")
                    print("\nHere is the upcoming attack: ")
                    for index, card in enumerate(hidden_upcoming):
                        if card is None:
                            print("None", end=" ")
                        else:
                            print(card.name, end=" ")
                    print("-> Hidden attack")
                    print()
                    end_sigil = True

                elif selected_sigil == "Swift":
                    print(f"\nYour {curr_hero[choice - 1].name} now has 50% chance to avoid attack")
                    if random.randint(0, 1) == 1:
                        curr_hero[choice - 1].barrier = True   
                    end_sigil = True 

                elif selected_sigil == "Shell":
                    while not end_sigil:
                        print("Which current attack card do you want to pick to cut the damage in half? Slot 1, 2, 3, or 4")
                        choice_3 = check_input.range_int("Enter choice: ", 1, 4)
                        if curr_attack[choice_3 - 1] is not None:
                            curr_attack[choice_3 - 1].power //= 2
                            print(f"\n {curr_attack[choice_3 - 1].name} card has half the damage now")
                            end_sigil = True
                        else:
                            print("There are no card in that slot, pick somewhere else.")

                elif selected_sigil == "None":
                    print("\nThis card has no sigil")
                    break  
        else:
            print("There are no card in that slot, pick somewhere else.")

def battle(hero, villian):
    print("------------- Battle -------------")
    
    shrimp_count = 20
    my_shrimp = shrimp.Shrimp()

    hero_hand = []
    play_deck = copy.deepcopy(hero._deck)
    #play_deck = deck.Deck()

    play_deck.shuffle()

    for _ in range(4):
        hero_hand.append(random_card(play_deck))

    villian._deck.shuffle()
    
    scale = 0
    turn = 0
    hidden_upcoming = [None, None, None, None]
    upcoming_attack = [None, None, None, None]
    curr_attack =     [None, None, None, None]
    curr_hero =       [None, None, None, None]



    while scale > -5 and scale < 5:
        if len(play_deck) -1 < 0:
            scale == -5
        
        # villian turn
        if turn == 0:
            print("\n---- Villain Turn ----\n")
            scale = villian_turn(villian, upcoming_attack, curr_attack, curr_hero, hidden_upcoming, scale)
            pause()
            turn = 1
        # Hero turn
        else:
            print("\n---- Hero Turn ----\n")
            scale = hero_turn(hero_hand, play_deck, shrimp_count, my_shrimp, curr_hero, scale, upcoming_attack, hidden_upcoming, curr_attack,villian, hero)
            pause()
            turn = 0

    if scale <= -5:
        clear_terminal()
        delay_print(f"Game Over You Drowned\n")
        death_messages(curr_attack)
        pause()
        choice = check_input.yes_no("Try again? Y/N\n")
        if choice is True:
            battle(hero, villian)
        else:
            exit()
    elif scale >= 5:
        clear_terminal()
        delay_print(f"You have defeated the evil {villian._name}\n You can move forward!")
        pause()
        clear_terminal()
