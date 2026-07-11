from random import randint
import json


name = ""
choice = ""
data = {}
all_data = []


def welcome():
    global name
    name = input("hello my friend.what's your name? ")
    print(f"welcome to this game {name}.i hope you enjoy this game")


def choose_difficulty():
    while True:
        print("\nChoose difficulty level:")
        print("1. Easy (10 guesses)")
        print("2. Hard (7 guesses)")
        global choice
        choice = input("Enter 1 or 2: ")

        if choice == "1":
            return 10
        elif choice == "2":
            return 7
        else:
            print("Please enter 1 or 2!")


def play():
    computer_number = randint(1, 99)
    max_attempts = choose_difficulty()
    counter = 0
    while True:
        try:
            guess_number = int(input("what's your guess?(range 1 to 99)\n"))
        except ValueError:
            print("please enter a valid number!")
            continue
        if guess_number == computer_number:
            counter += 1
            print("********** hamed : you are win **********")
            print(f"number of guesses : {counter}")
            global data
            data = {"name": name, "record": counter}
            return True
        elif guess_number > computer_number:
            counter += 1
            print("The number you guessed is greater than the computer's number.")
            print(f"number of guesses : {counter}")
        elif guess_number < computer_number:
            counter += 1
            print("The number you guessed is smaller than the computer's number.")
            print(f"number of guesses : {counter}")
        if counter >= max_attempts:
            print("———- hamed : you are lost ———- ")
            return False


def save_record():
    global all_data
    flag = 0
    try:
        if choice == "1":
            file_address = (
                "E:/simple project/number guessing/save_records_easy_level.json"
            )
        else:
            file_address = (
                "E:/simple project/number guessing/save_records_hard_level.json"
            )
    except Exception as e:
        return f"error : {e}"

    try:
        try:
            with open(file_address, "r") as sr:
                all_data = json.load(sr)
        except (json.JSONDecodeError, FileNotFoundError):
            all_data = []

        user_found = False
        for i in range(len(all_data)):
            if all_data[i]["name"] == name:
                user_found = True
                if data["record"] < all_data[i]["record"]:
                    all_data[i]["record"] = data["record"]
                    flag = 1
                break

        if not user_found:
            all_data.append(data)

        for _ in range(len(all_data)):
            for best_record in range(1, len(all_data)):
                if (
                    all_data[best_record]["record"]
                    < all_data[best_record - 1]["record"]
                ):
                    all_data[best_record - 1], all_data[best_record] = (
                        all_data[best_record],
                        all_data[best_record - 1],
                    )

        with open(file_address, "w") as sr:
            json.dump(all_data, sr, indent=4, sort_keys=True)
    except Exception as e:
        print(f"error : {e}")


def show_best_record():
    global all_data
    if len(all_data) == 0:
        print("No records available yet.")
        return

    best_record = all_data[0]["record"]
    record_holders = []
    for i in range(len(all_data)):
        if all_data[i]["record"] == best_record:
            record_holders.append(all_data[i]["name"])
        else:
            break
    print(f"best record : {best_record}")
    print(f"record holders : {record_holders}")


def main():
    global all_data
    all_data = []

    while True:
        welcome()
        if play():
            save_record()
            show_best_record()
        answer = input("if you want play again? y/n ")
        while answer.lower() not in ["y", "n"]:
            answer = input("if you want play again? y/n ")
        if answer.lower() == "y":
            pass
        else:
            print("thanks for playing. bye")
            break


if __name__ == "__main__":
    main()
