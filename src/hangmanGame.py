import requests
import random

endgame= '''
                     888                                      
                     888                                      
                     888                                      
 .d88b. 88888b.  .d88888 .d88b.  8888b. 88888b.d88b.  .d88b.  
d8P  Y8b888 "88bd88" 888d88P"88b    "88b888 "888 "88bd8P  Y8b 
88888888888  888888  888888  888.d888888888  888  88888888888 
Y8b.    888  888Y88b 888Y88b 888888  888888  888  888Y8b.     
 "Y8888 888  888 "Y88888 "Y88888"Y888888888  888  888 "Y8888  
                             888                              
                        Y8b d88P                              
                         "Y88P"  '''
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
def hangman():

    attemps = 0
    result = ""
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
    print('''| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/''')

    response = requests.get(word_site)
    WORDS = response.content.splitlines()
    word_selected = str(random.choice(WORDS))
    word_selected = word_selected.replace("b'", "").replace("'","")
    print(word_selected)


    for n in word_selected:
        result += "_"
    print(result)


    while result.find("_") !=-1:
        letter = input("\nIntroduce a letter: ")
        if letter.lower() in word_selected.lower():
            for index in range(len(word_selected)):
                if word_selected[index] == letter:
                    result = result[:index] + word_selected[index] + result[index + 1:]
            print(result)
        else:
            if attemps == len(HANGMANPICS):
                print(endgame)
                print(f"The correct word was: {word_selected}")
                break
            else:
                print(HANGMANPICS[attemps])
                attemps += 1
    if result.find("_") == -1:
        print('''
██╗░░░██╗░█████╗░██╗░░░██╗  ░██╗░░░░░░░██╗██╗███╗░░██╗
╚██╗░██╔╝██╔══██╗██║░░░██║  ░██║░░██╗░░██║██║████╗░██║
░╚████╔╝░██║░░██║██║░░░██║  ░╚██╗████╗██╔╝██║██╔██╗██║
░░╚██╔╝░░██║░░██║██║░░░██║  ░░████╔═████║░██║██║╚████║
░░░██║░░░╚█████╔╝╚██████╔╝  ░░╚██╔╝░╚██╔╝░██║██║░╚███║
░░░╚═╝░░░░╚════╝░░╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝''')











