from os import system
from time import sleep


def welcome():
    print("hello my friends.what's your name? ")
    global player1, player2
    player1 = input("first player : ")
    player2 = input("second player : ")
    print(f"welcome to this game {player1} and {player2}. i hope you enjoy this game")
    answer = input("are you ready?(y/n) ")
    while answer.lower() not in ["y", "n"]:
        print("please enter the answer carefully.")
        answer = input("are you ready?(y/n)")
    if answer.lower() == "y":
        pass
    else:
        return False
    system("cls")
    for s in range(3, 0, -1):
        print(s)
        sleep(1)
        system("cls")
    return True


def play():
    count = 1
    player1_score = 0
    player2_score = 0
    while count <= 5:
        player1_choose = int(
            input(
                "the first player chooses the number ==> [scissor = 1] , [rock = 2], [paper = 3] : "
            )
        )
        system("cls")
        while not 1 <= player1_choose <= 3:
            print("please enter the number carefully.")
            player1_choose = int(
                input(
                    "the first player chooses the number ==> [scissor = 1] , [rock = 2], [paper = 3] : "
                )
            )
            system("cls")
        player2_choose = int(
            input(
                "the second player chooses the number ==> [scissor = 1] , [rock = 2], [paper = 3] : "
            )
        )
        system("cls")
        while not 1 <= player2_choose <= 3:
            print("please enter the number carefully.")
            player2_choose = int(
                input(
                    "the second player chooses the number ==> [scissor = 1] , [rock = 2], [paper = 3] : "
                )
            )
            system("cls")
        if player1_choose == player2_choose:
            pass
        elif player2_choose == 1 and player1_choose == 2:
            player1_score += 1
        elif player2_choose == 1 and player1_choose == 3:
            player2_score += 1
        elif player2_choose == 2 and player1_choose == 3:
            player1_score += 1
        elif player2_choose == 2 and player1_choose == 1:
            player2_score += 1
        elif player2_choose == 3 and player1_choose == 1:
            player1_score += 1
        elif player2_choose == 3 and player1_choose == 2:
            player2_score += 1
        print(f"round {count}")
        print(f"The first player's chosen number : {player1_choose}")
        print(f"The second player's chosen number : {player2_choose}")
        print(
            f"player points : \nplayer1 {player1} : {player1_score} \nplayer2 {player2} : {player2_score}"
        )
        sleep(3)
        system("cls")
        count += 1
    if player1_score > player2_score:
        print(f"--The first player {player1} wins--")
    elif player2_score > player1_score:
        print(f"--The second player {player2} wins--")
    else:
        print("the game ended in a tie.")


def main():
    while True:
        if not welcome():
            print("ok!. no problem. when you ready, run this program")
            break
        play()
        answer = input("do you want play again?(y/n)")
        while answer.lower() not in ["y", "n"]:
            print("please enter the answer carefully.")
            answer = input("do you want play again?(y/n)")
        if answer.lower() == "y":
            pass
        else:
            print("thanks for playing")
            break


if __name__ == "__main__":
    main()
