import time
from random import choice

keywordDict={
    'cities':['Egypt','London','Albania','Japan','Dubai','Italy'],
    'sports':['Vollyball','Tennis','Pingpong','Basketball','Football'],
    'boysNames':['Ahmed','Ali','John','Mohanad','Kareem'],
    'girlsNames':['Mai','Toka','Asmaa','Mariam'],
    'rondomWords':['Boy','girl','sports','cities','Hello','Hangman'],
}

def ShowInfo():
    print("\nWelcome To ' H A N G M A N ' Game!")
    time.sleep(1)
    Hangman(3)
    time.sleep(1)
    name = input("Please Enter Your Name: ")
    time.sleep(0.5)
    print(f"Hello {name.upper()} , Best of Luck!\n")
    time.sleep(0.5)
    print("Let's Play HANGMAN!")
    time.sleep(0.5)
    print("The game is about to start!\n")
    time.sleep(1)
    print("Select An Category")
    time.sleep(1)
    print("  1: Cities")
    time.sleep(0.5)
    print("  2: Sports")
    time.sleep(0.5)
    print("  3: Boys Names")
    time.sleep(0.5)
    print("  4: Girls Names")
    time.sleep(0.5)
    print("  5: Random Words")
    time.sleep(0.5)
    print("  6: Exit From The Game\n")
    time.sleep(0.5)

def GetcategoryOption():
    ShowInfo()
    try:
        categoryOption = int(input('Please Enter A Category Option: '))
        if categoryOption>=1 and categoryOption<=5:
            return categoryOption
        elif categoryOption==6:
            print('\nTHANKS FOR Using H A N G M A N !\nSEE YOU IN THE NEXT TIME ')
        else:
            print('INVALID INPUT! PLEASE TRY AGAIN..\n')
            GetcategoryOption()
    except:
        print('ERORR OCCURED! PLEASE TRY AGAIN..\n')
        GetcategoryOption()

def GetWordFromChoosedCategory(categoryOption):
    if categoryOption >=1 and categoryOption<=5:
        if categoryOption == 1:
            return choice(keywordDict['cities'])
        elif categoryOption == 2:
            return choice(keywordDict['sports'])
        elif categoryOption == 3:
            return choice(keywordDict['boysNames'])
        elif categoryOption == 4:
            return choice(keywordDict['girlsNames'])
        elif categoryOption == 5:
            return choice(keywordDict['rondomWords'])

def Hangman(numberOfTries):
    if numberOfTries == 3:
        time.sleep(1)
        print("       _____   \n"
              "      |     |  \n"
              "      |     |  \n"
              "      |     |  \n"
              "      |     O  \n"
              "      |    /|\ \n"
              "    __|__  / \ \n")
    elif numberOfTries==2:
        time.sleep(1)
        print("       _____   \n"
              "      |     |  \n"
              "      |     |  \n"
              "      |     O  \n"
              "      |    /|\ \n"
              "      |    / \ \n"
              "    __|__      \n")
    elif numberOfTries==1:
        time.sleep(1)
        print("       _____   \n"
              "      |     |  \n"
              "      |     O  \n"
              "      |    /|\ \n"
              "      |    / \ \n"
              "      |        \n"
              "    __|__      \n")
    elif numberOfTries==0:
        time.sleep(1)
        print("\n      ***        *      **      ** ******       *****  *       * ******  ****   \n")
        time.sleep(0.5)
        print("     *         *   *    *  *   * * *           *     *  *     *  *      *     * \n")
        time.sleep(0.5)
        print("     *  ***   *     *   *    *   * ******      *     *   *   *   ****** * ***   \n")
        time.sleep(0.5)
        print("     *    *  * ***** *  *        * *           *     *    * *    *      *  *    \n")
        time.sleep(0.5)
        print("      ***   *         * *        * ******       *****      *     ****** *    *  \n")
        time.sleep(0.5)

def PlayingLoop():
    word=GetWordFromChoosedCategory(GetcategoryOption()).upper()
    guesses = []
    Lives=3
    guessed=False

    while not guessed:
        for letter in word:
            if letter.upper() in guesses:
                print(letter,end="")
            else:
                print('_',end=" ")

        guess=input(f"\n\n{Lives} Lives Left, Next Guess: ").upper()
        if not guess.isalpha():
            print ('INVALID INPUT!, Letters Only')
        else:
            guesses.append(guess.upper())
            if guess.upper() not in word:
                Lives-=1
                if Lives !=0:
                    print("Try Harder!\n")
            else:
                print("Nice Try!\n")
            Hangman(Lives)

            if Lives ==0:
                print(f"\n{Lives} Lives Left!")
                break

            done = True
            for letter in word:
                if letter.upper() not in guesses:
                    guessed=False
    if guessed:
        print(f"You Found The Word,It Was: {word} !")
    else:
        print(f'GAME OVER! The Word Was: {word} \nTry Harder Next Time..\n\n')

def ContinueOrExitTheGame():
    flag=True
    while flag:
        time.sleep(0.5)
        flag=int(input("Do You Want To Play Again\n  0: No\n  1: Yes\nPlease Enter Your Option: "))
        if flag==0:
            print('\nTHANKS FOR Using H A N G M A N !\nSEE YOU IN THE NEXT TIME ')
            break
        elif flag==1:
            PlayingLoop()
        else:
            print('INVALID INPUT! PLEASE TRY AGAIN..\n')

def Main():
    try:
        PlayingLoop()
        ContinueOrExitTheGame()
    except:
        print("\n")

Main()