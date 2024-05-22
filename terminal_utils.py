import os
import sys
import time

def clear_terminal():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    """Pauses the program until the user presses Enter."""
    input("Press Enter to continue...")

def delay_print(text, delay=0.04):
    """Prints the text with a delay between characters."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def delay_input(text, delay=0.04):
    delay_print(text, delay=delay)
    return input()

def delay(delay=0.1):
    time.sleep(delay)
