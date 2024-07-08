import map
import player
import battle 
import random
import check_input
from terminal_utils import clear_terminal, pause, delay_print, delay
from boss_file import boss, boss_battle

def welcome_message(name):
    
    delay_print(f"\nWelcome to AquaScrypt {name}! \n")
    delay_print("Will you make it back to the surface with undiscovered treasures?...")
    delay_print("or will the sea consume you...")
    delay(1.5)
    delay_print(f"\nWell {name}, good luck diving!\n")
    print("Made by Hamster Chips Inc.")

def How_to_play():
    quit = False 
    while quit is False:
        print("\n1. Battle Guide\n2. Map Guide\n3. Sigil Guide\n4. Shop Item Guide\n5. Upgrade Guide\n6. Sacrifice Guide\n7. Quit")
        choice = check_input.range_int("Choice: ",1,7)
        guide_files = {
            1: 'guide_file/battle.txt',
            2: 'guide_file/map_guide.txt',
            3: 'guide_file/sigil_guide.txt',
            4: 'guide_file/shop_item_guide.txt',
            5: 'guide_file/upgrade_guide.txt',
            6: 'guide_file/sacrifice_guide.txt'
        }

        if choice == 7:
            print("\nQuitting the guide.\n")
            quit = True 
        
        file = guide_files.get(choice)

        if file:
            with open(file, "r") as file:
                print(file.read())
                print()
                pause()
                clear_terminal()
    
def main():
    clear_terminal()
    print("~~~ AquaScrypt ~~~")
    quit = False
    vaild = False 
    while vaild is False:
        print("1. New game\n2. Load game\n3. How to play!\n4. Quit")
        choice = check_input.range_int("Choice: ", 1, 4)
        if choice == 1:
            # delay_print("What is your name, diver? ")
            # name = input("Name: ")
            # welcome_message(name)
            #name = "Joe"
            hero = player.Player(load=False)
            vaild = True
        elif choice == 2:
            hero = player.Player(load=True)
            vaild = True

        elif choice == 3:
            How_to_play()
        else: 
            vaild = True
            exit()

    print(f"\nWell hello, {hero.name}")
    print("\nHere is your current items: ")
    hero.display_items()
    print("\n\nHere is your current deck: ")
    hero.display_deck()
    print()
    
    villian = boss.Boss("Abyssal Soldier")
    game_map = map.Map()
    game_map.load_map("map1", "map1.txt")
    next_map = 0
    boss_def = 0

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
            else: 
                print("Well alright ... Your funeral")
            quit = True 

        clear_terminal()

        if move == 'I':
            hero.shop_item()

        elif move == 'U':
            hero._deck.upgrade()

        elif move == 'V':
            battle.battle(hero, villian)

        elif move == 'A':
            hero._deck.sacrifice()

        elif move == 'B':
            if boss_def == 0:
                bubble = boss.Boss("Bubble Bass")
                boss_battle.boss_battle(hero, bubble)
                boss_def +=1

            elif boss_def == 1:
                scuba = boss.Boss("Scuba Diver")
                boss_battle.boss_battle(hero, scuba)
                boss_def +=1

            else:
                mermaid = boss.Boss("Seraphina, Empress of the Abyss")
                boss_battle.boss_battle(hero, mermaid)
        
        elif move == '?':
            random_num = random.randint(1,5)
            if random_num == 1:
                hero.shop_item()

            elif random_num == 2:
                hero._deck.upgrade()

            elif random_num == 3:
                battle.battle(hero, villian)

            elif random_num == 4:  
                hero._deck.sacrifice()

            else:
                print("Nothing happens. You may proceed.\n")

        elif move == 'D':
            clear_terminal()

            rand = random.randint(1, 3)
            if rand == 1:
                item = "Dagger"
            elif rand == 2:
                item = "Boulder"
            elif rand == 3:
                item = "Shrimp Bottle"
            hero._items.append(item)
            delay_print(f"You encounter a {item} while heading down to the abyss....\n")

            if next_map == 0:
                game_map.load_map("map2", "map2.txt")
                delay_print("You may advance, but beware you will soon approach the abyss.\nProceed with caution!")
                pause()
                clear_terminal()
                game_map.switch_map("map2",hero)
                next_map +=1

            else:
                game_map.load_map("map3", "map3.txt")
                delay_print("As you drew closer to the abyss, a haunting noise grew louder.\nYou have reached the abyss. Brace yourself, for the true trials begin now.")
                pause()
                clear_terminal()
                game_map.switch_map("map3",hero)

        elif move == "F":
            delay_print(f"You have reached the end and defeated the boss.\n Your journey has come to a victorious close. Well done, {hero.name}!!!")
            exit()
                   
        print()
main()