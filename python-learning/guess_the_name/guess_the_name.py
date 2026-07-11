from random import choice
import json


def welcome():
    global name
    name = input("hello my friend. what's your name? ")
    print(f"Welcome to this game {name}. I hope you enjoy playing this game.")


def get_words():
    print(
        "You have to enter ten words so that the computer can guess your chosen word from them."
    )
    global words
    words = []
    count = 1
    while count <= 10:
        word = input(f"enter word {count} : ")
        words.append(word)
        count += 1


def play():
    print("please choose a word from the list.")
    selected_words = []
    global counter
    counter = 0
    while True:
        selected_word = choice(words)
        if selected_word in selected_words:
            continue
        elif len(selected_words) == len(words):
            print(
                "The word you selected was probably not on the list because none of the words on the list were your chosen word."
            )
            break
        print(f"is your word {selected_word}?y/n")
        answer = input()
        if answer.lower() in ["y", "yes"]:
            counter += 1
            print(f"Hooray! I found the word after {counter} guessing.")
            break
        elif answer in ["n", "no"]:
            if selected_word not in selected_words:
                selected_words.append(selected_word)
            counter += 1
        else:
            pass
        if len(selected_words) == len(words):
            print(
                "The word you selected was probably not on the list because none of the words on the list were your chosen word."
            )
            break
    global data
    data = {"name": name, "record": counter}


def save_records():
    global all_data
    try:
        try:
            with open(
                "E:/simple project/Guess the name (game)/save_records.json", "r"
            ) as sr:
                all_data = json.load(sr)
        except (json.JSONDecodeError, FileNotFoundError):
            all_data = []
        all_data.append(data)
        for _ in range(len(all_data)):
            for best_record in range(1, len(all_data)):
                if (
                    all_data[best_record]["record"]
                    > all_data[best_record - 1]["record"]
                ):
                    all_data[best_record], all_data[best_record - 1] = (
                        all_data[best_record - 1],
                        all_data[best_record],
                    )
        with open(
            "E:/simple project/Guess the name (game)/save_records.json", "w"
        ) as sr:
            json.dump(all_data, sr, indent=4, sort_keys=True)
    except Exception as e:
        print(f"error : {e}")


def show_best_record():
    best_record = all_data[0]["record"]
    record_holders = []
    for names in range(len(all_data)):
        if all_data[names]["record"] == best_record:
            record_holders.append(all_data[names]["name"])
    print(f"Record holders of the game so far : {record_holders}")


def main():
    while True:
        welcome()
        get_words()
        play()
        save_records()
        show_best_record()
        print("if you want play again?y/n")
        answer = input()
        while answer.lower() not in ["y", "yes", "n", "no"]:
            print("if you want play again?y/n")
            answer = input()
        if answer.lower() in ["y", "yes"]:
            pass
        elif answer.lower() in ["n", "no"]:
            break


if __name__ == "__main__":
    main()
