import deck
import card
import map
import random
import json
import check_input
from terminal_utils import clear_terminal, pause, delay_print, delay_input, delay

class Player():
    def __init__(self, load=False):
        if not load:
            self._name = input("\nWhat is your name? ")
            self._items = []
            self._location = [5, 2]
            self._deck = deck.Deck()
        else:
            print("\nWhich load file would you like to use 1, 2, or 3")
            load_choice = check_input.range_int("Choice: ", 1, 3)
            with open(f"player{load_choice}.json", "r") as files:
                data = json.load(files)
                self._name = data["player_name"]
                self._items = data["items"]
                self._location = data["location"]
                self._deck = [card.Card(**card_data) for card_data in data["deck"]]
        
    @property
    def name(self):
        return self._name

    @property
    def location(self):
        return self._location
    
    def display_items(self):
        for item in self._items:
            print(item, end=" ")

    def display_deck(self):
        count = 0
        for card in self._deck:
            print(f"{count}. {card.name}")
            count += 1

    def save_game(self, file_name):
        player_data = {
            "player_name": self._name,
            "items": self._items,
            "location": self._location,
            "deck": [card.serialize() for card in self._deck]
        }

    def shop_item(self):
        print("Welcome to meh shop! \nPick whichever tickles your fancy!\n")
        print("1. Dagger - Cut out your eye and place it on scale, giving you one points toward victory.")
        print("2. Boulder - Place it to block enemies attack up to 5 hit points")
        print("3. Shrimp Bottle - A shrimp will go right into your hand")

        done = False
        while not done:
            choice = input("Your choice: ")
            if choice == "1":
                self._items.append("Dagger")
                done = True
            elif choice == "2":
                self._items.append("Boulder")
                done = True
            elif choice == "3":
                self._items.append("Shrimp Bottle")
                done = True
            else:
                print("Invalid input - between 1 - 3")
            
        print("\nYour current items:", " ".join(self._items))
        print()
        pause()
        clear_terminal()

    def __str__(self):
        return f"Name: {self._name} \nItems: {self.displayItems()} \nDeck: {self.display_deck()}"
  
    def go_forward(self):
        m = map.Map()
        if len(self._location) - 1 < len(m) - 1:
            if self._location[0] > 0 and m[self.location[0] - 1][self.location[1]] != "-":
                self._location[0] -= 1
                return m[self.location[0]][self.location[1]]
            else:
                print("\nYou cannot go that way\n")
                return 'o'
        return 'o'

    def go_right(self):
        m = map.Map()
        if len(self._location) - 1 < len(m) - 1:
            if self._location[1] < 4 and self._location[0] > 0 and m[self.location[0] - 1][self.location[1] + 1] != "-":
                self._location[1] += 1
                self._location[0] -= 1 
                return m[self.location[0]][self.location[1]]
            else:
                print("\nYou cannot go that way\n")
                return 'o'
        else:
            return 'o'

    def go_left(self):
        m = map.Map()
        if len(self._location) - 1 < len(m) - 1:
            if self._location[1] > 0 and self._location[0] > 0 and m[self.location[0] - 1][self.location[1] - 1] != "-":
                self._location[1] -= 1
                self._location[0] -= 1
                return m[self.location[0]][self.location[1]]
            else:
                print("\nYou cannot go that way\n")
                return 'o'
        else:
            return 'o'
