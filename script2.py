import time


def rules():
    print("\n"*20)
    print("\t"*20, "You will be player1 if you want to mark first and your opponent be player2!\n\n")
    time.sleep(1)
    print("\t"*20, "Rules: Player1 marks 'X' goes first \n")
    time.sleep(1)
    print("\t"*20, "       Player2 marks 'O' goes second\n")
    time.sleep(1)


def wanna_start():
    print("\n" * 20)
    print("\t"*20, end='')
    return input("Are you ready to play? Enter Yes or No.") in ["Yes", "yes", "YES", "y", "Y"]


def replay():
    print("\n" * 20)
    print("\t" * 20, end='')
    return input("Wanna Play?") not in ["Yes", "yes", "Y", "y"]