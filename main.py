import map
import player
import battle 
import deck
import check_input
from terminal_utils import clear_terminal, pause, delay_print, delay_input, delay
from boss_file import boss

def welcome_message(name):
    
    delay_print(f"\nWelcome to AquaScrypt {name}! \n")
    delay_print("Will you make it back to the surface with undiscovered treasures?...")
    delay_print("or will the sea consume you...")
    delay(1.5)
    delay_print(f"\nWell {name}, good luck diving!\n")

def main():
    clear_terminal()
    print("~~~ AquaScrypt ~~~")
    print("1. New game\n2. Load game\n3. Quit")
    quit = False 
    choice = check_input.range_int("Choice: ", 1, 3)
    if choice == 1:
        # delay_print("What is your name, diver? ")
        # name = input("Name: ")
        # welcome_message(name)
        #name = "Joe"
        hero = player.Player(False)
    elif choice == 2:
        hero = player.Player(True)
    else: 
        quit = True

    print(f"\nWell hello, {hero.name}")
    print("\nHere is your current items: ")
    hero.display_items()
    print("\n\nHere is your current deck: ")
    hero.display_deck()
    print()
    
    villian = boss.Boss("Jeff")
    game_map = map.Map()

    pause()
    clear_terminal()
    while not quit :
        print(game_map.show_map(hero.location))
        print("1. Go stright\n2. Go left\n3. Go right\n4. Quit")
        menu_choice = input("Enter choice: ")

        move = ''
        if menu_choice == "1":
            move = hero.go_forward()
        elif menu_choice == "2":
            move = hero.go_left()
        elif menu_choice == "3":
            move = hero.go_right()
        elif menu_choice == "4":
            print("Would you like to save your progress?")
            if check_input.yes_no("Y/N: "):
                print("Would you like to save in slot 1, 2, or 3")
                save_choice = check_input.range_int("Choice: ", 1, 3)
                file_name = f"player{save_choice}"
                hero.save_game(file_name)
            quit = True 

        clear_terminal()

        if move == 'I':
            hero.shop_item()
        elif move == 'U':
            clear_terminal()
            hero._deck.upgrade()
        elif move == 'B':
            battle.battle(hero, villian)
        elif move == 'A':
            hero._deck.sacrifice()

        # print("Would you like to save your game?")
        # if check_input.yes_no("Choice: "):
        #     print("Would like to save in slot 1, 2, or 3")
        #     num = check_input.range_int("Choice: ", 1, 3)
        #     hero.save_game(num)
        # else:
        #     print("Well alright ... Your funeral")
        
        print()
main()