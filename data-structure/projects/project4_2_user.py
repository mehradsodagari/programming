from project4_1 import Stack
import keyboard
import os
import time


class Maze:
    def __init__(self, side_length):
        self.side_length = side_length
        self.routes = []

    def create_table(self):
        rows = []
        for row in range(self.side_length):
            for column in range(self.side_length):
                element = int(input(f"enter the {(row,column)} element : "))
                while element not in [0, 1]:
                    element = int(input(f"enter the {(row,column)} element : "))
                os.system("cls")
                rows.append(element)
            self.routes.append(rows)
            rows = []
        return "the table was created"

    def show_table(self):
        for i in self.routes:
            print(i)

    def find_route(self):
        try:
            s = Stack()
            if self.routes[0][0] == 1:
                return False
            count = 0
            row = 0
            column = 0
            s.push_item((row, column))
            coordinates = [(row, column)]
            while True:
                time.sleep(0.2)
                if row == self.side_length - 1 and column == self.side_length - 1:
                    break
                os.system("cls")
                self.show_table()
                print(f"cooredinate : {coordinates[-1]}")
                if keyboard.is_pressed("up"):
                    if row - 1 >= 0 and self.routes[row - 1][column] == 0:
                        if (row - 1, column) not in s.items:
                            row -= 1
                            s.push_item((row, column))
                            coordinates.append((row, column))
                        count = 0
                        continue
                    else:
                        count += 1
                        print("Cannot move in that direction! (Wall or boundary)")
                        time.sleep(1)
                elif keyboard.is_pressed("down"):
                    if row + 1 < self.side_length and self.routes[row + 1][column] == 0:
                        if (row + 1, column) not in s.items:
                            row += 1
                            s.push_item((row, column))
                            coordinates.append((row, column))
                        count = 0
                        continue
                    else:
                        count += 1
                        print("Cannot move in that direction! (Wall or boundary)")
                        time.sleep(1)
                elif keyboard.is_pressed("right"):
                    if (
                        column + 1 < self.side_length
                        and self.routes[row][column + 1] == 0
                    ):
                        if (row, column + 1) not in s.items:
                            column += 1
                            s.push_item((row, column))
                            coordinates.append((row, column))
                        count = 0
                        continue
                    else:
                        count += 1
                        print("Cannot move in that direction! (Wall or boundary)")
                        time.sleep(1)
                elif keyboard.is_pressed("left"):
                    if column - 1 >= 0 and self.routes[row][column - 1] == 0:
                        if (row, column - 1) not in s.items:
                            column -= 1
                            s.push_item((row, column))
                            coordinates.append((row, column))
                        count = 0
                        continue
                    else:
                        count += 1
                        print("Cannot move in that direction! (Wall or boundary)")
                        time.sleep(1)
                else:
                    continue
                if (
                    1 <= row <= self.side_length - 2
                    and 1 <= column <= self.side_length - 2
                    and count == 4
                ):
                    break
                elif (
                    row in [0, self.side_length - 1]
                    or column in [0, self.side_length - 1]
                ) and count == 2:
                    break
                elif (
                    row in [0, self.side_length - 1]
                    or column not in [0, self.side_length - 1]
                ) and count == 3:
                    break
                elif (
                    row not in [0, self.side_length - 1]
                    or column in [0, self.side_length - 1]
                ) and count == 3:
                    break
                elif row == self.side_length - 1 and column == self.side_length - 1:
                    s.push_item((row, column))
                    break
            if s.items[-1] != (self.side_length - 1, self.side_length - 1):
                return False
            s.reverse()
            for index in range(len(s.items) - 1):
                print(s.items[index], end=" -> ")
            print(s.items[-1])
            return True
        except Exception as e:
            return f"error : {e}"


m = Maze(5)
m.create_table()
print(m.find_route())
