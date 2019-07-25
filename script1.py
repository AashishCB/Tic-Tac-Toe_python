from script2 import *
import time


def mark(turn):
    if turn % 2 == 0:
        print_board(t1, t2, t3)
        print("\n\n", "\t" * 20,"Player 1:Choose your position:", end='')
        pos = int(input())
        pos_on_board = dy[pos]
        if pos_on_board[0:2] == "t1":
            t1[int(pos_on_board[3])] = "X"
        elif pos_on_board[0:2] == "t2":
            t2[int(pos_on_board[3])] = "X"
        elif pos_on_board[0:2] == "t3":
            t3[int(pos_on_board[3])] = "X"
        if check():
            return [True, "Player 1 wins"]
        else:
            return [False]
    else:
        print_board(t1, t2, t3)
        print("\n\n", "\t" * 20, "Player 2:Choose your position:", end='')
        pos = int(input())
        pos_on_board = dy[pos]
        if pos_on_board[0:2] == "t1":
            t1[int(pos_on_board[3])] = "O"
        elif pos_on_board[0:2] == "t2":
            t2[int(pos_on_board[3])] = "O"
        elif pos_on_board[0:2] == "t3":
            t3[int(pos_on_board[3])] = "O"
        if check():
            return [True, "Player 2 wins"]
        else:
            return [False]


def check():
    return (t1[0] == t1[2] == t1[4] == "X") or (t2[0] == t2[2] == t2[4] == "X") or (t3[0] == t3[2] == t3[4] == "X") or \
           (t1[0] == t2[0] == t3[0] == "X") or (t1[2] == t2[2] == t3[2] == "X") or (t1[4] == t2[4] == t3[4] == "X") or \
           (t1[0] == t2[2] == t3[4] == "X") or (t1[4] == t2[2] == t3[0] == "X") or (t1[0] == t1[2] == t1[4] == "O") or \
           (t2[0] == t2[2] == t2[4] == "O") or (t3[0] == t3[2] == t3[4] == "O") or (t1[0] == t2[0] == t3[0] == "O") or \
           (t1[2] == t2[2] == t3[2] == "O") or (t1[4] == t2[4] == t3[4] == "O") or (t1[0] == t2[2] == t3[4] == "O") or \
           (t1[4] == t2[2] == t3[0] == "O")


def print_board(x, y, z):
    print("\n" * 100)
    print("\t" * 15, "".join(z), "\t" * 15, "".join(t6))
    print("\t" * 15, "-----------", "\t" * 15, "-----------")
    print("\t" * 15, "".join(y), "\t" * 15, "".join(t5))
    print("\t" * 15, "-----------", "\t" * 15, "-----------")
    print("\t" * 15, "".join(x), "\t" * 15, "".join(t4))


dy = {1: "t1[0]", 2: "t1[2]", 3: "t1[4]", 4: "t2[0]", 5: "t2[2]", 6: "t2[4]", 7: "t3[0]", 8: "t3[2]", 9: "t3[4]"}
# creating the three list for making the input number format of tic tac toe box
t6 = ["7", "  | ", "8", " | ", "9"]
t5 = ["4", "  | ", "5", " | ", "6"]
t4 = ["1", "  | ", "2", " | ", "3"]
# The welcome part
print("\n"*10, "                                                                       WELCOME \n")
print("                                                                           TO\n")
print("                                                                      TIC TAC TOE!\n\n\n\n")
time.sleep(3)
print("\n"*10)
# Introducing the format
print("                            This is the format                        ", "".join(t6))
print("                            you should give input!                    ", "-----------")
print("                            Picking the box number                    ", "".join(t5))
print("                            and entering it!                          ", "-----------")
print("                                                                      ", "".join(t4),"\n\n\n\n")
time.sleep(3)
# Starting the game
while True:

    # The tic tac toe box form marking
    t3 = [" ", "  | ", " ", " | ", " "]
    t2 = [" ", "  | ", " ", " | ", " "]
    t1 = [" ", "  | ", " ", " | ", " "]

    #  function imported from script2
    rules()
    #  function imported from script2
    if wanna_start():
        i = 0
        while i < 9:
            b = mark(i)
            print_board(t1, t2, t3)
            i += 1
            if b[0]:
                print("\n\n", "\t"*20, b[1])
                time.sleep(2)
                break
        else:
            print("\n\n", "\t"*20, "No wins")
            time.sleep(2)
    else:
        print("\n\n", "\t"*20, "Alright")
        time.sleep(2)
    # function imported from script2
    if replay():
        print("\n"*20, "\t"*20, "ok bye")
        break
