from tabulate import tabulate
from emoji import emojize
from os import system, path
from time import sleep
from datetime import datetime
from colorama import Fore
from pathlib import Path
from random import choice, random
from playsound import playsound
from copy import copy
import threading
import platform
import json


class TicTacToe:
    def __init__(self, first_player="", second_player=""):
        self.first_player = first_player
        self.second_player = second_player
        self.numbers = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
        self.first_player_char = "⨯"
        self.second_player_char = "○"
        self.first_player_color = Fore.RED
        self.second_player_color = Fore.BLUE
        self.winner = ""
        self.menu = {
            "1": "two player game",
            "2": "one player game",
            "3": "show standings",
            "4": "view game history",
            "5": "replay match",
            "6": "overall game statistics",
            "7": "setting",
            "8": "exit",
        }
        self.sounds_route = Path(__file__).parent / "sounds"
        self.final_table = None
        self.chosen_numbers = []

    def welcoming(self):
        print(Fore.WHITE + "* " * 23 + Fore.RESET)
        print(Fore.WHITE + "*                                           *" + Fore.RESET)
        print(
            Fore.WHITE
            + f"*       {Fore.LIGHTBLUE_EX}       tic tac toe      {Fore.RESET}            *"
            + Fore.RESET
        )
        print(Fore.WHITE + "*                                           *" + Fore.RESET)
        print(
            Fore.WHITE
            + f"*     {Fore.LIGHTBLUE_EX}   created by : mehrad sodagari   {Fore.RESET}    *"
            + Fore.RESET
        )
        print(Fore.WHITE + "*                                           *" + Fore.RESET)
        print(
            Fore.WHITE
            + f"*        {Fore.LIGHTBLUE_EX}      lets go play        {Fore.RESET}         *"
            + Fore.RESET
        )
        print(Fore.WHITE + "*                                           *" + Fore.RESET)
        print(Fore.WHITE + "* " * 23 + Fore.RESET)
        sleep(3)
        self.safe_play((self.sounds_route / "start.mp3"))
        self.clean_screen()
        return

    def safe_play(self, sound_file):
        if not sound_file.exists():
            return

        def play():
            try:
                playsound(str(sound_file), block=True)
            except:
                pass

        threading.Thread(target=play, daemon=True).start()

    def table(self):
        try:
            colored_table = []
            for row in self.numbers:
                new_row = []
                for cell in row:
                    new_row.append(self.colored_cell(cell))
                colored_table.append(new_row)
            return tabulate(colored_table, tablefmt="heavy_grid")
        except Exception as e:
            return f"error : {e}"

    def get_current_player(self, turn):
        try:
            if turn % 2 == 0:
                return self.first_player
            return self.second_player
        except Exception as e:
            return f"error : {e}"

    def get_current_char(self, turn):
        try:
            return self.first_player_char if turn % 2 == 0 else self.second_player_char
        except Exception as e:
            return f"error : {e}"

    def change_number_with_character(self, turn, number):
        try:
            position = {
                "1": (0, 0),
                "2": (0, 1),
                "3": (0, 2),
                "4": (1, 0),
                "5": (1, 1),
                "6": (1, 2),
                "7": (2, 0),
                "8": (2, 1),
                "9": (2, 2),
            }
            row, column = position[number]
            self.numbers[row][column] = self.get_current_char(turn)
            return
        except Exception as e:
            return f"error : {e}"

    def colored_cell(self, character):
        try:
            if character == self.first_player_char:
                return self.first_player_color + self.first_player_char + Fore.RESET
            elif character == self.second_player_char:
                return self.second_player_color + self.second_player_char + Fore.RESET
            return character
        except Exception as e:
            return f"error : {e}"

    def clean_screen(self):
        try:
            if platform.system() == "Windows":
                system("cls")
            else:
                system("clear")
        except Exception as e:
            return f"error : {e}"

    def win(self):
        try:
            winning = [
                [self.numbers[0][0], self.numbers[0][1], self.numbers[0][2]],
                [self.numbers[1][0], self.numbers[1][1], self.numbers[1][2]],
                [self.numbers[2][0], self.numbers[2][1], self.numbers[2][2]],
                [self.numbers[0][0], self.numbers[1][0], self.numbers[2][0]],
                [self.numbers[0][1], self.numbers[1][1], self.numbers[2][1]],
                [self.numbers[0][2], self.numbers[1][2], self.numbers[2][2]],
                [self.numbers[0][0], self.numbers[1][1], self.numbers[2][2]],
                [self.numbers[2][0], self.numbers[1][1], self.numbers[0][2]],
            ]
            for line in winning:
                if line[0] == line[1] == line[2] and line[0] in [
                    self.first_player_char,
                    self.second_player_char,
                ]:
                    return True
            return False
        except Exception as e:
            return f"error : {e}"

    def available_moves(self, board):
        try:
            available = []
            for row in range(3):
                for column in range(3):
                    if board[row][column] not in ["○", "⨯"]:
                        available.append((row, column))
            return available
        except Exception as e:
            return f"error : {e}"

    def check_winner_for_minimax(self, board, player_char):
        try:
            winning = [
                [board[0][0], board[0][1], board[0][2]],
                [board[1][0], board[1][1], board[1][2]],
                [board[2][0], board[2][1], board[2][2]],
                [board[0][0], board[1][0], board[2][0]],
                [board[0][1], board[1][1], board[2][1]],
                [board[0][2], board[1][2], board[2][2]],
                [board[0][0], board[1][1], board[2][2]],
                [board[2][0], board[1][1], board[0][2]],
            ]
            for line in winning:
                if line[0] == line[1] == line[2] and line[0] == player_char:
                    return True
            return False
        except Exception as e:
            return f"error : {e}"

    def board_is_full(self, board):
        try:
            for row in range(3):
                for column in range(3):
                    if board[row][column] not in ["○", "⨯"]:
                        return False
            return True
        except Exception as e:
            return f"error : {e}"

    def position_to_number(self, row, col):
        try:
            positions = {
                (0, 0): "1",
                (0, 1): "2",
                (0, 2): "3",
                (1, 0): "4",
                (1, 1): "5",
                (1, 2): "6",
                (2, 0): "7",
                (2, 1): "8",
                (2, 2): "9",
            }
            return positions.get((row, col))
        except Exception as e:
            return f"error : {e}"

    def find_best_move(self):
        try:
            if not self.available_moves(self.numbers):
                return
            best_score = -float("inf")
            best_move = None
            board = [row[:] for row in self.numbers]
            for move in self.available_moves(board):
                row, col = move
                original = board[row][col]
                board[row][col] = "○"
                score = self.minimax(board, 0, False)
                board[row][col] = original
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
            return best_move
        except Exception as e:
            return f"error : {e}"

    def minimax(self, board, depth, is_maximizing):
        try:
            if self.second_player == "computer":
                if self.check_winner_for_minimax(board, "○"):
                    return 10 - depth
                if self.check_winner_for_minimax(board, "⨯"):
                    return depth - 10
            else:
                if self.check_winner_for_minimax(board, "⨯"):
                    return 10 - depth
                if self.check_winner_for_minimax(board, "○"):
                    return depth - 10
            if self.board_is_full(board):
                return 0
            if self.second_player == "computer":
                if is_maximizing:
                    current_player_char = "○"
                else:
                    current_player_char = "⨯"
            else:
                if is_maximizing:
                    current_player_char = "⨯"
                else:
                    current_player_char = "○"
            if is_maximizing:
                best_score = float("-inf")
            else:
                best_score = float("inf")
            for move in self.available_moves(board):
                row, col = move
                original_value = board[row][col]
                board[row][col] = current_player_char
                score = self.minimax(board, depth + 1, not is_maximizing)
                board[row][col] = original_value
                if is_maximizing:
                    best_score = max(score, best_score)
                else:
                    best_score = min(score, best_score)
            return best_score
        except Exception as e:
            return f"error : {e}"

    def play(self):
        try:
            turn = 0
            available_option = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            while True:
                print(self.table())
                if turn % 2 == 0:
                    number = input(
                        Fore.WHITE
                        + f"{self.first_player} ({self.first_player_char}). choose one of these option. options : {available_option} (q to quit)\n"
                        + Fore.RESET
                    )
                    if number == "q":
                        self.clean_screen()
                        exit()
                    while number not in available_option:
                        print(
                            Fore.YELLOW
                            + f"pay attention {self.first_player} ({self.first_player_char}), this number is not among the options"
                            + Fore.RESET
                        )
                        number = input(
                            f"{self.first_player} ({self.first_player_char}).choose one of these option. options : {available_option} (q to quit)\n"
                        )
                    if number == "q":
                        self.clean_screen()
                        exit()
                    self.chosen_numbers.append(number)
                    available_option.remove(number)
                else:
                    print(
                        Fore.WHITE
                        + f"{self.second_player} ({self.second_player_char}). choose one of these option. options : {available_option} (q to quit)\n"
                        + Fore.RESET
                    )
                    number = input()
                    if number == "q":
                        self.clean_screen()
                        exit()
                    while number not in available_option:
                        print(
                            Fore.YELLOW
                            + f"pay attention {self.second_player} ({self.second_player_char}), this number is not among the options"
                            + Fore.RESET
                        )
                        print(
                            Fore.WHITE
                            + f"{self.second_player} ({self.second_player_char}). choose one of these option. options : {available_option} (q to quit)\n"
                            + Fore.RESET
                        )
                        number = input()
                    if number == "q":
                        self.clean_screen()
                        exit()
                    self.chosen_numbers.append(number)
                    available_option.remove(number)
                self.safe_play(self.sounds_route / "move.wav")
                self.change_number_with_character(turn, number)
                turn += 1
                if self.win():
                    self.clean_screen()
                    print(self.table())
                    self.winner = self.get_current_player(turn - 1)
                    self.safe_play(self.sounds_route / "win.wav")
                    print(
                        emojize(
                            Fore.GREEN
                            + f"{self.winner} win game :partying_face:. congratulation"
                            + Fore.RESET
                        )
                    )
                    self.final_table = [row[:] for row in self.numbers]
                    return
                elif not available_option and not self.win():
                    print(self.table())
                    self.safe_play(self.sounds_route / "tie.wav")
                    print(Fore.YELLOW + "the game was tied" + Fore.RESET)
                    self.final_table = [row[:] for row in self.numbers]
                    return
                self.clean_screen()
        except Exception as e:
            print(f"error : {e}")
            return

    def first_move(self):
        try:
            move = choice(["player", "computer"])
            if move == "computer":
                return True
            return False
        except Exception as e:
            return f"error : {e}"

    def play_vs_computer_easy_level(self):
        try:
            flag = 0
            if self.first_move():
                self.first_player_char = "○"
                self.second_player_char = "⨯"
                self.first_player_color = Fore.BLUE
                self.second_player_color = Fore.RED
                turn = 1
                flag = 1
            else:
                self.first_player_char = "⨯"
                self.second_player_char = "○"
                self.first_player_color = Fore.RED
                self.second_player_color = Fore.BLUE
                turn = 0
                flag = 0
            human_name = "Mehrad"
            try:
                setting_path = Path(__file__).parent / "setting.json"
                with open(setting_path, "r", encoding="utf-8") as f:
                    setting = json.load(f)
                human_name = setting.get("name", "Player")
            except:
                human_name = "Player"
            available_option = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            while True:
                print(self.table())
                if turn % 2 == 0:
                    print(
                        Fore.WHITE
                        + f"{human_name} ({self.second_player_char if flag==1 else self.first_player_char}). choose one of these option. options : {available_option} (q to quit)\n"
                        + Fore.RESET
                    )
                    number = input()
                    if number == "q":
                        self.clean_screen()
                        exit()
                    while number not in available_option:
                        print(
                            Fore.YELLOW
                            + f"pay attention {human_name} ({self.second_player_char if flag==1 else self.first_player_char}), this number is not among the options"
                            + Fore.RESET
                        )
                        number = input(
                            Fore.WHITE
                            + f"{human_name} ({self.second_player_char if flag==1 else self.first_player_char}). choose one of these option. options : {available_option} (q to quit)\n"
                            + Fore.RESET
                        )
                    if number == "q":
                        self.clean_screen()
                        exit()
                    self.chosen_numbers.append(number)
                    available_option.remove(number)
                else:
                    number = choice(available_option)
                    number = str(number)
                    print(
                        Fore.WHITE
                        + f"computer ({self.first_player_char if flag==1 else self.second_player_char}) is thinking..."
                        + Fore.RESET
                    )
                    sleep(1)
                    self.chosen_numbers.append(number)
                    available_option.remove(number)
                self.safe_play(self.sounds_route / "move.wav")
                self.change_number_with_character(turn, number)
                turn += 1
                if self.win():
                    self.clean_screen()
                    print(self.table())
                    self.winner = self.get_current_player(turn - 1)
                    self.safe_play(self.sounds_route / "win.wav")
                    if self.winner == self.first_player:
                        print(
                            emojize(
                                Fore.GREEN
                                + "you win the game :partying_face:"
                                + Fore.RESET
                            )
                        )
                    else:
                        print(
                            emojize(
                                Fore.RED
                                + "you lost the game!!! :loudly_crying_face:"
                                + Fore.RESET
                            )
                        )
                    self.final_table = [row[:] for row in self.numbers]
                    return
                elif not available_option and not self.win():
                    print(self.table())
                    self.safe_play(self.sounds_route / "lose.wav")
                    print(
                        emojize(
                            Fore.YELLOW
                            + "the game was tied!!! :neutral_face:"
                            + Fore.RESET
                        )
                    )
                    self.winner = "tie"
                    self.final_table = [row[:] for row in self.numbers]
                    return
                self.clean_screen()
        except Exception as e:
            print(f"error : {e}")
            return

    def play_vs_computer_medium_level(self):
        try:
            flag = 0
            if self.first_move():
                self.first_player_char = "○"
                self.second_player_char = "⨯"
                self.first_player_color = Fore.BLUE
                self.second_player_color = Fore.RED
                turn = 1
                flag = 1
            else:
                self.first_player_char = "⨯"
                self.second_player_char = "○"
                self.first_player_color = Fore.RED
                self.second_player_color = Fore.BLUE
                turn = 0
                flag = 0
            human_name = "Mehrad"
            try:
                setting_path = Path(__file__).parent / "setting.json"
                with open(setting_path, "r", encoding="utf-8") as f:
                    setting = json.load(f)
                human_name = setting.get("name", "Player")
            except:
                human_name = "Player"
            available_option = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            while True:
                print(self.table())
                if turn % 2 == 0:
                    print(
                        Fore.WHITE
                        + f"{human_name} ({self.second_player_char if flag==1 else self.first_player_char}). choose one of these option. options : {available_option} (q to quit)\n"
                        + Fore.RESET
                    )
                    number = input()
                    if number == "q":
                        self.clean_screen()
                        exit()
                    while number not in available_option:
                        print(
                            Fore.YELLOW
                            + f"pay attention {human_name} ({self.second_player_char if flag==1 else self.first_player_char}), this number is not among the options"
                            + Fore.RESET
                        )
                        number = input(
                            Fore.WHITE
                            + f"{human_name} ({self.second_player_char if flag==1 else self.first_player_char}). choose one of these option. options : {available_option} (q to quit)\n"
                            + Fore.RESET
                        )
                    if number == "q":
                        self.clean_screen()
                        exit()
                    self.chosen_numbers.append(number)
                    available_option.remove(number)
                else:
                    if random() < 0.5:
                        best_move = self.find_best_move()
                        row, col = best_move
                        number = self.position_to_number(row, col)
                        print(
                            Fore.WHITE
                            + f"computer ({self.first_player_char if flag==1 else self.second_player_char}) is thinking..."
                            + Fore.RESET
                        )
                        sleep(1)
                        self.chosen_numbers.append(number)
                        available_option.remove(number)
                    else:
                        number = choice(available_option)
                        number = str(number)
                        print(
                            Fore.WHITE
                            + f"computer ({self.first_player_char if flag==1 else self.second_player_char}) is thinking..."
                            + Fore.RESET
                        )
                        sleep(1)
                        self.chosen_numbers.append(number)
                        available_option.remove(number)
                self.safe_play(self.sounds_route / "move.wav")
                self.change_number_with_character(turn, number)
                turn += 1
                if self.win():
                    self.clean_screen()
                    print(self.table())
                    self.winner = self.get_current_player(turn - 1)
                    self.safe_play(self.sounds_route / "win.wav")
                    if self.winner == self.first_player:
                        print(
                            emojize(
                                Fore.GREEN
                                + "you win the game :partying_face:"
                                + Fore.RESET
                            )
                        )
                    else:
                        print(
                            emojize(
                                Fore.RED
                                + "you lost the game!!! :loudly_crying_face:"
                                + Fore.RESET
                            )
                        )
                    self.final_table = [row[:] for row in self.numbers]
                    return
                elif not available_option and not self.win():
                    print(self.table())
                    self.safe_play(self.sounds_route / "lose.wav")
                    print(
                        emojize(
                            Fore.YELLOW
                            + "the game was tied! :neutral_face:"
                            + Fore.RESET
                        )
                    )
                    self.winner = "tie"
                    self.final_table = [row[:] for row in self.numbers]
                    return
                self.clean_screen()
        except Exception as e:
            print(f"error : {e}")
            return

    def play_vs_computer_hard_level(self):
        try:
            flag = 0
            if self.first_move():
                self.first_player_char = "○"
                self.second_player_char = "⨯"
                self.first_player_color = Fore.BLUE
                self.second_player_color = Fore.RED
                turn = 1
                flag = 1
            else:
                self.first_player_char = "⨯"
                self.second_player_char = "○"
                self.first_player_color = Fore.RED
                self.second_player_color = Fore.BLUE
                turn = 0
                flag = 0
            human_name = "Mehrad"
            try:
                setting_path = Path(__file__).parent / "setting.json"
                with open(setting_path, "r", encoding="utf-8") as f:
                    setting = json.load(f)
                human_name = setting.get("name", "Player")
            except:
                human_name = "Player"
            available_option = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            while True:
                print(self.table())
                if turn % 2 == 0:
                    print(
                        Fore.WHITE
                        + f"{human_name} ({self.second_player_char if flag==1 else self.first_player_char}). choose one of these option. options : {available_option} (q to quit)\n"
                        + Fore.RESET
                    )
                    number = input()
                    if number == "q":
                        self.clean_screen()
                        exit()
                    while number not in available_option:
                        print(
                            Fore.YELLOW
                            + f"pay attention {human_name} ({self.second_player_char if flag==1 else self.first_player_char}), this number is not among the options"
                            + Fore.RESET
                        )
                        number = input(
                            Fore.WHITE
                            + f"{human_name} ({self.second_player_char if flag==1 else self.first_player_char}). choose one of these option. options : {available_option} (q to quit)\n"
                            + Fore.RESET
                        )
                    if number == "q":
                        self.clean_screen()
                        exit()
                    self.chosen_numbers.append(number)
                    available_option.remove(number)
                else:
                    best_move = self.find_best_move()
                    if best_move is None:
                        if available_option:
                            number = choice(available_option)
                        else:
                            break
                    row, col = best_move
                    number = self.position_to_number(row, col)
                    print(
                        Fore.WHITE
                        + f"computer ({self.first_player_char if flag==1 else self.second_player_char}) is thinking..."
                        + Fore.RESET
                    )
                    sleep(1)
                    self.chosen_numbers.append(number)
                    available_option.remove(number)
                self.safe_play(self.sounds_route / "move.wav")
                self.change_number_with_character(turn, number)
                turn += 1
                if self.win():
                    self.clean_screen()
                    print(self.table())
                    self.winner = self.get_current_player(turn - 1)
                    self.safe_play(self.sounds_route / "win.wav")
                    if self.winner == self.first_player:
                        print(
                            emojize(
                                Fore.GREEN
                                + "you win the game :partying_face:. \nyou are a genius"
                                + Fore.RESET
                            )
                        )
                    else:
                        print(
                            emojize(
                                Fore.RED
                                + "you lost the game :loudly_crying_face: you were great"
                                + Fore.RESET
                            )
                        )
                    self.final_table = [row[:] for row in self.numbers]
                    return
                elif not available_option and not self.win():
                    print(self.table())
                    self.safe_play(self.sounds_route / "lose.wav")
                    print(
                        emojize(
                            Fore.YELLOW
                            + "the game was tied :neutral_face: \ngood job"
                            + Fore.RESET
                        )
                    )
                    self.winner = "tie"
                    self.final_table = [row[:] for row in self.numbers]
                    return
                self.clean_screen()
        except Exception as e:
            print(f"error : {e}")
            return

    def reset_board(self):
        try:
            self.numbers = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
            self.chosen_numbers = []
            self.winner = ""
            self.final_table = None
            self.first_player_char = "⨯"
            self.second_player_char = "○"
            self.first_player_color = Fore.RED
            self.second_player_color = Fore.BLUE
        except Exception as e:
            return f"error : {e}"

    def save_match_details(self):
        try:
            match_data = {
                "player 1": self.first_player,
                "player 2": self.second_player,
                "winner": self.winner if self.winner != "" else "tie",
                "date and time match": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "final_table": self.final_table,
                "chosen_numbers": self.chosen_numbers,
                "first_player_character": self.first_player_char,
                "second_player_character": self.second_player_char,
                "first_player_color": str(self.first_player_color),
                "second_player_color": str(self.second_player_color),
            }
            file_path = Path(__file__).parent / "matches.json"
            if path.exists(file_path):
                with open(file_path, "r", encoding="utf-8") as f:
                    history = json.load(f)
            else:
                history = []
            history.append(match_data)
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(history, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"error : {e}")

    def save_record_holders(self):
        try:
            file_path = Path(__file__).parent / "winners.json"
            if path.exists(file_path):
                with open(file_path, "r", encoding="utf-8") as f:
                    history = json.load(f)
            else:
                history = {}
            if self.winner and self.winner != "" and self.winner != "tie":
                if self.winner in history:
                    history[self.winner] += 1
                else:
                    history[self.winner] = 1
            history = {
                k: v
                for k, v in sorted(
                    history.items(), key=lambda item: item[1], reverse=True
                )
            }
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(history, f, ensure_ascii=False)
        except Exception as e:
            print(f"error : {e}")

    def show_leadertable(self):
        try:
            route = Path(__file__).parent
            file_path = route / "winners.json"
            if not path.exists(file_path):
                default_data = {} if file_path.name == "winners.json" else []
                with open(file_path, "w", encoding="utf-8") as f:
                    json.dump(default_data, f, ensure_ascii=False)
            with open(file_path, "r", encoding="utf-8") as f:
                history = json.load(f)
            if not history:
                print(Fore.WHITE + "no one has won yet" + Fore.RESET)
            else:
                rank = 1
                rows = []
                for person, record in history.items():
                    rows.append([rank, person, record])
                    rank += 1
                print(
                    tabulate(
                        rows, headers=["rank", "name", "record"], tablefmt="heavy_grid"
                    )
                )
            user_input = input("press Enter to continue... (q to quit)\n")
            if user_input == "q":
                self.clean_screen()
                exit()
        except Exception as e:
            print(f"error : {e}")

    def show_match_history(self):
        try:
            route = Path(__file__).parent
            file_path = route / "matches.json"
            if not path.exists(file_path):
                default_data = [] if file_path.name == "matches.json" else {}
                with open(file_path, "w", encoding="utf-8") as f:
                    json.dump(default_data, f, ensure_ascii=False)
            with open(file_path, encoding="utf-8") as f:
                history = json.load(f)
            if not history:
                print(Fore.WHITE + "no game has been played yet" + Fore.RESET)
                user_input = input("press Enter to continue... (q to quit)\n")
                if user_input == "q":
                    self.clean_screen()
                    exit()
                return
            rows = []
            game = 1
            for match in history:
                rows.append(
                    [
                        game,
                        match["player 1"],
                        match["player 2"],
                        match["winner"],
                        match["date and time match"],
                    ]
                )
                game += 1
            game_number = 1
            for match in history:
                self.clean_screen()
                print(
                    tabulate(
                        rows,
                        headers=[
                            "game",
                            "player 1",
                            "player 2",
                            "winner",
                            "date and time match",
                        ],
                        tablefmt="heavy_grid",
                    )
                )
                print(f"final_table (match {game_number}):")
                print(tabulate(match["final_table"], tablefmt="heavy_grid"))
                user_input = input("press Enter to continue... (q to quit)\n")
                if user_input == "q":
                    self.clean_screen()
                    exit()
                game_number += 1
                sleep(0.5)
                self.clean_screen()
            return
        except Exception as e:
            print(f"error : {e}")
            return

    def show_player_status(self, player_name):
        try:
            route = Path(__file__).parent
            file_path = route / "matches.json"
            with open(file_path, "r", encoding="utf-8") as f:
                history = json.load(f)
            win = 0
            tie = 0
            loss = 0
            for match in history:
                if match["player 1"] == player_name or match["player 2"] == player_name:
                    if match["winner"] == player_name:
                        win += 1
                    elif match["winner"] == "tie":
                        tie += 1
                    else:
                        loss += 1
            if win == 0 and tie == 0 and loss == 0:
                print(Fore.WHITE + f"{player_name} hasn't played yet" + Fore.RESET)
            else:
                print(f"{Fore.WHITE}{player_name} status {Fore.RESET}")
                print(f"{Fore.GREEN}win : {win}{Fore.RESET}")
                print(f"{Fore.YELLOW}tie : {tie}{Fore.RESET}")
                print(f"{Fore.RED}loss : {loss}{Fore.RESET}")
                print(
                    f"{Fore.WHITE}winning percentage : {(win/(win+tie+loss))*100:.1f}%{Fore.RESET}"
                )
            user_input = input("press Enter to continue... (q to quit)\n")
            if user_input == "q":
                self.clean_screen()
                exit()
            self.clean_screen()
        except Exception as e:
            return f"error : {e}"

    def replay(self):
        replay_board = TicTacToe()
        try:
            route = Path(__file__).parent
            file_path = route / "matches.json"
            with open(file_path, "r", encoding="utf-8") as f:
                history = json.load(f)
            if not history:
                print("no games available for replay")
                user_input = input("press Enter to continue... (q to quit)\n")
                if user_input == "q":
                    self.clean_screen()
                    exit()
                return
            print(
                f"what game do you want to watch? (So far {len(history)} games played)  (q to quit)\n"
            )
            try:
                what_game = input()
                if what_game == "q":
                    self.clean_screen()
                    exit()
                what_game = int(what_game)
            except ValueError:
                print("please enter a valid number")
                sleep(2)
                return
            if what_game < 1 or what_game > len(history):
                print(
                    f"invalid game number. please choose between 1 and {len(history)}"
                )
                sleep(2)
                return
            match = history[what_game - 1]
            replay_board.first_player = match["player 1"]
            replay_board.second_player = match["player 2"]
            replay_board.first_player_char = match["first_player_character"]
            replay_board.second_player_char = match["second_player_character"]

            def get_color_from_code(color_code):
                try:
                    color_map = {
                        "\x1b[31m": Fore.RED,
                        "\x1b[34m": Fore.BLUE,
                        "\x1b[36m": Fore.CYAN,
                        "\x1b[32m": Fore.GREEN,
                        "\x1b[33m": Fore.YELLOW,
                        "\x1b[35m": Fore.MAGENTA,
                        "\x1b[37m": Fore.WHITE,
                        "\x1b[94m": Fore.LIGHTBLUE_EX,
                        "\x1b[91m": Fore.LIGHTRED_EX,
                    }
                    return color_map.get(color_code, Fore.RED)
                except Exception as e:
                    return f"error : {e}"

            replay_board.first_player_color = get_color_from_code(
                match["first_player_color"]
            )
            replay_board.second_player_color = get_color_from_code(
                match["second_player_color"]
            )
            print(
                f"{replay_board.first_player} sign is: {replay_board.first_player_char}"
            )
            print(
                f"{replay_board.second_player} sign is: {replay_board.second_player_char}"
            )
            print("starting replay...")
            sleep(2)
            replay_board.clean_screen()
            moves = match["chosen_numbers"]
            turn = 0
            move_number = 1
            for move in moves:
                print(f"move {move_number}: position {move}")
                print(replay_board.table())
                replay_board.change_number_with_character(turn, move)
                turn += 1
                move_number += 1
                sleep(2)
                replay_board.clean_screen()
            print("final board:")
            print(replay_board.table())
            print(f"result: {match['winner']}")
            user_input = input("press Enter to continue...  (q to quit)\n")
            if user_input == "q":
                self.clean_screen()
                exit()
            replay_board.clean_screen()
        except Exception as e:
            print(f"error : {e}")
            sleep(2)

    def overall_game_statistics(self):
        try:
            file_path = Path(__file__).parent / "matches.json"
            with open(file_path, "r", encoding="utf-8") as f:
                history = json.load(f)
            if not history:
                print("no game has been played yet")
                user_input = input("press Enter to continue... (q to quit)\n")
                if user_input == "q":
                    self.clean_screen()
                    exit()
                return
            matches = 0
            win_x = 0
            win_o = 0
            tie = 0
            list_consecutive_wins = []
            consecutive_wins = 0
            for match in history:
                if match["winner"] != "tie":
                    consecutive_wins += 1
                    if match["winner"] == match["player 1"]:
                        if match["first_player_character"] == "⨯":
                            win_x += 1
                        else:
                            win_o += 1
                    elif match["winner"] == match["player 2"]:
                        if match["first_player_character"] == "⨯":
                            win_o += 1
                        else:
                            win_x += 1
                    else:
                        tie += 1
                    list_consecutive_wins.append(consecutive_wins)
                else:
                    consecutive_wins = 0
                    tie += 1
                    list_consecutive_wins.append(consecutive_wins)
                matches += 1
            best_record = max(list_consecutive_wins) if list_consecutive_wins else 0
            print(Fore.WHITE + "overall game statistics : " + Fore.RESET)
            print(Fore.LIGHTCYAN_EX + f"total match played : {matches}")
            print(
                Fore.GREEN
                + f"win percentage with ⨯ : {(win_x/matches)*100:.0f}"
                + Fore.RESET
            )
            print(
                Fore.GREEN
                + f"win percentage with ○ : {(win_o/matches)*100:.0f}"
                + Fore.RESET
            )
            print(
                Fore.YELLOW + f"tie percentage : {(tie/matches)*100:.0f}" + Fore.RESET
            )
            print(
                Fore.LIGHTBLUE_EX
                + f"best consecutive win record : {best_record}"
                + Fore.RESET
            )
            user_input = input("press Enter to continue... (q to quit)\n")
            if user_input == "q":
                self.clean_screen()
                exit()
            return
        except Exception as e:
            return f"error : {e}"

    def change_settings(self):
        try:
            file_path = Path(__file__).parent / "settings.json"
            default = {"name": "player", "sound": "on"}
            if path.exists(file_path):
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        setting = json.load(f)
                except:
                    setting = default.copy()
            else:
                setting = default.copy()
            print(f"welcome to setting {setting['name'] if setting['name'] else None}")
            for i in setting:
                print(f"{i}. {setting[i]}")
            print("options :")
            print("1.change name ")
            print("2.sounds ")
            what_do = input("what do want to do?(1 or 2) (q to quit)\n")
            self.clean_screen()
            if what_do == "q":
                self.clean_screen()
                exit()
            while what_do not in ["1", "2"]:
                print("1.change name ")
                print("2.sounds ")
                what_do = input("what do you want to do?(1 or 2) (q to quit)\n")
                if what_do == "q":
                    self.clean_screen()
                    exit()
            if what_do == "1":
                name = input("enter new name :\n")
                setting["name"] = name
                self.clean_screen()
            else:
                sound = input("on or off\n")
                self.clean_screen()
                if sound == "q":
                    self.clean_screen()
                    exit()
                while sound.lower() not in ["on", "off"]:
                    sound = input("on or off\n")
                    self.clean_screen()
                    if sound == "q":
                        self.clean_screen()
                        exit()
                if sound == "on":
                    setting["sound"] = "on"
                else:
                    setting["sound"] = "off"
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(setting, f, indent=4, ensure_ascii=False)
            print(Fore.GREEN + "setting saved successfully" + Fore.RESET)
        except Exception as e:
            return f"error : {e}"

    def sound(self):
        try:
            file_path = Path(__file__).parent / "settings.json"
            if file_path.exists():
                with open(file_path, "r", encoding="utf-8") as f:
                    setting = json.load(f)
                return setting.get("sound", "on") == "on"
            return True
        except:
            return True


def main():
    try:
        Game = TicTacToe()
        Game.welcoming()
        Game.clean_screen()
        while True:
            rows = []
            for key, value in Game.menu.items():
                rows.append(
                    [
                        f"{Fore.LIGHTCYAN_EX}{key}{Fore.RESET}",
                        f"{Fore.WHITE}{value}{Fore.RESET}",
                    ]
                )
            print(
                tabulate(
                    rows,
                    headers=[
                        f"{Fore.YELLOW}Option{Fore.RESET}",
                        f"{Fore.YELLOW}Description{Fore.RESET}",
                    ],
                    tablefmt="fancy_grid",
                    stralign="center",
                    colalign=("center", "left"),
                )
            )
            choice = input(
                Fore.WHITE + "enter your desired option (q to quit)\n" + Fore.RESET
            )
            if choice == "q":
                Game.clean_screen()
                exit()
            while choice not in Game.menu:
                print("please enter the desired option carefully" + Fore.RESET)
                choice = input("enter your desired option (q to quit)\n")
                if choice == "q":
                    Game.clean_screen()
                    exit()
            Game.clean_screen()
            if choice == "1":
                while True:
                    First_player = input(
                        Fore.WHITE
                        + "enter first player name :  (q to quit)\n"
                        + Fore.RESET
                    )
                    if First_player == "q":
                        Game.clean_screen()
                        exit()
                    Game.first_player = First_player
                    Game.clean_screen()
                    Second_player = input(
                        Fore.WHITE
                        + "enter second player name :  (q to quit)\n"
                        + Fore.RESET
                    )
                    if Second_player == "q":
                        Game.clean_screen()
                        exit()
                    Game.second_player = Second_player
                    Game.clean_screen()
                    Game.clean_screen()
                    Game.show_player_status(First_player)
                    Game.clean_screen()
                    Game.show_player_status(Second_player)
                    Game.clean_screen()
                    Game.play()
                    Game.save_match_details()
                    Game.save_record_holders()
                    Game.reset_board()
                    print(
                        Fore.WHITE
                        + "do you want play again?(y/n) (q to quit)\n"
                        + Fore.RESET
                    )
                    answer = input()
                    if answer == "q":
                        Game.clean_screen()
                        exit()
                    Game.clean_screen()
                    while answer.lower() not in ["y", "n"]:
                        print(
                            Fore.WHITE
                            + "do you want play again?(y/n)  (q to quit)\n"
                            + Fore.RESET
                        )
                        answer = input()
                        if answer == "q":
                            Game.clean_screen()
                            exit()
                        Game.clean_screen()
                    if answer == "y":
                        Game.clean_screen()
                        pass
                    else:
                        Game.clean_screen()
                        break
                    sleep(2)
            elif choice == "2":
                while True:
                    Player = "player"
                    try:
                        setting_path = Path(__file__).parent / "settings.json"
                        with open(setting_path, "r", encoding="utf-8") as f:
                            setting = json.load(f)
                        Player = setting.get("name", "Player")
                    except:
                        Player = "player"
                    Game.first_player = Player
                    Game.second_player = "computer"
                    Game.clean_screen()
                    game_level = input(
                        "what level do you want play? 1.easy or 2.medium or 3.hard (q to quit)\n"
                    )
                    if game_level == "q":
                        Game.clean_screen()
                        exit()
                    while game_level not in ["1", "2", "3"]:
                        Game.clean_screen()
                        print("please enter your desired level carefully")
                        game_level = input(
                            "what level do you want play? 1.easy or 2.medium or 3.hard (q to quit)\n"
                        )
                        if game_level == "q":
                            Game.clean_screen()
                            exit()
                    Game.clean_screen()
                    Game.show_player_status(Player)
                    if game_level == "1":
                        Game.clean_screen()
                        Game.play_vs_computer_easy_level()
                    elif game_level == "2":
                        Game.clean_screen()
                        Game.play_vs_computer_medium_level()
                    else:
                        for _ in range(3):
                            print(Fore.LIGHTRED_EX + "UNBEATABLE AI" + Fore.RESET)
                            sleep(0.3)
                            Game.clean_screen()
                            sleep(0.3)
                        Game.clean_screen()
                        Game.play_vs_computer_hard_level()
                    sleep(2)
                    Game.clean_screen()
                    Game.save_match_details()
                    Game.save_record_holders()
                    Game.reset_board()
                    print(
                        Fore.WHITE
                        + "do you want play again?(y/n) (q to quit)\n"
                        + Fore.RESET
                    )
                    answer = input()
                    if answer == "q":
                        Game.clean_screen()
                        exit()
                    Game.clean_screen()
                    while answer.lower() not in ["y", "n"]:
                        print(
                            Fore.WHITE
                            + "do you want play again?(y/n) (q to quit)\n"
                            + Fore.RESET
                        )
                        answer = input()
                        if answer == "q":
                            Game.clean_screen()
                            exit()
                        Game.clean_screen()
                    if answer == "y":
                        Game.clean_screen()
                        pass
                    else:
                        Game.clean_screen()
                        break
            elif choice == "3":
                Game.show_leadertable()
            elif choice == "4":
                Game.show_match_history()
            elif choice == "5":
                Game.replay()
            elif choice == "6":
                Game.overall_game_statistics()
            elif choice == "7":
                Game.change_settings()
                sleep(1)
                Game.clean_screen()
            elif choice == "8":
                print(
                    emojize(
                        Fore.MAGENTA
                        + "thanks for playing this Game :red_heart: . bye"
                        + Fore.RESET
                    )
                )
                sleep(2)
                Game.clean_screen()
                break
    except Exception as e:
        print(f"error : {e}")


if __name__ == "__main__":
    main()
