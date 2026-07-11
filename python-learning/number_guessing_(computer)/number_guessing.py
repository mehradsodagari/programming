from random import randint


def welcome():
    name = input("hello my dear. what's your name ? ")
    print(f"welcome to this game {name}. i hope you enjoy this game.")


def play():
    try:
        target = int(input("please enter a number from 1 to 99 : "))
        while not 1 <= target <= 99:
            print("number not in range 1 to 99")
            target = int(input("please enter a number from 1 to 99 : "))
        start = 1
        end = 99
        while True:
            computer_guess = randint(start, end)
            if computer_guess == target:
                print(f" *** computer is win —- number is : {target} ***")
                break
            print(f"computer guess : {computer_guess}")
            user_input = input("computer guess up(u) or down(d) : ")
            while user_input.lower() not in ["u", "d"]:
                print("please enter u or d")
                user_input = input("computer guess up(u) or down(d): ")
            if user_input.lower() == "u":
                end = computer_guess - 1
            else:
                start = computer_guess + 1
    except Exception as e:
        print(f"error : {e}")


def main():
    welcome()
    while True:
        play()
        print("if you want play again?(y/n)")
        answer = input()
        while answer.lower() not in ["y", "n"]:
            print("please answer the question carefully.")
            print("do you want play again?y/n")
            answer = input()
        if answer.lower() == "y":
            pass
        elif answer.lower() == "n":
            print("thanks for playing")
            break


if __name__ == "__main__":
    main()
