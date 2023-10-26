# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from src import gameRockPaperScissors, passwordGenerator, hangmanGame, caesarCipher
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    def menu_principal():
        print("Welcome to the principal menu")
        print("1. Game Rock, Paper, Scissors")
        print("2. Password Generator")
        print("3. Hangman Game")
        print("4. Caesar Cypher")

        option = int(input("Seleccione una opción: "))

        if option == 1:
            gameRockPaperScissors.game()
        elif option == 2:
            passwordGenerator.generator()
        elif option == 3:
            hangmanGame.hangman()
        elif option == 4:
            caesarCipher.cipher()
        else:
            print("Invalid option")

    menu_principal()
