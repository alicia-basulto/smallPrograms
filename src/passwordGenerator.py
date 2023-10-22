import random
import string
from colorama import Fore, Style

def get_user_input(prompt):
    print(Fore.GREEN + prompt + Style.RESET_ALL, end='')
    user_input = input()
    return user_input

def generator():
    print('''
╦ ╦┌─┐┬  ┌─┐┌─┐┌┬┐┌─┐  ┌┬┐┌─┐                        
║║║├┤ │  │  │ ││││├┤    │ │ │                        
╚╩╝└─┘┴─┘└─┘└─┘┴ ┴└─┘   ┴ └─┘                        
┌─┐┌─┐┌─┐┌─┐┬ ┬┌─┐┬─┐┌┬┐  ┌─┐┌─┐┌┐┌┌─┐┬─┐┌─┐┌┬┐┌─┐┬─┐
├─┘├─┤└─┐└─┐││││ │├┬┘ ││  │ ┬├┤ │││├┤ ├┬┘├─┤ │ │ │├┬┘
┴  ┴ ┴└─┘└─┘└┴┘└─┘┴└──┴┘  └─┘└─┘┘└┘└─┘┴└─┴ ┴ ┴ └─┘┴└─
''')

    length = int(get_user_input("Introduce the length of your password: "))
    print("How many symbols would you like?")
    symbols = int(get_user_input("Symbols: "))
    print("How many symbols would you like?")
    letters = int(get_user_input("Letters: "))
    print("How many symbols would you like?")
    numbers = int(get_user_input("Numbers: "))
    letters_range = string.ascii_letters
    digits_range =  string.digits
    symbols_range = string.punctuation
    characters = ''.join(random.choice(letters_range) for _ in range(letters))
    characters += ''.join(random.choice(digits_range) for _ in range(numbers))
    characters += ''.join(random.choice(symbols_range) for _ in range(symbols))
    password = ''.join(random.choice(characters) for _ in range(length))

    print("Generated password:", password)