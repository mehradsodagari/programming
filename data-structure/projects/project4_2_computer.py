from project4_1 import Stack
import os
from copy import copy


class Maze:
    def __init__(self, side_length):
        self.side_length = side_length
        self.routes = []
        self.all_routes = []

    def create_table(self):
        rows = []
        for row in range(self.side_length):
            for column in range(self.side_length):
                element = int(input(f"enter the {(row,column)} element : "))
                while element not in [0, 1]:
                    element = int(input(f"enter the {(row,column)} element : "))
                rows.append(element)
            self.routes.append(rows)
            rows = []
        return "the table was created"

    def show_table(self):
        for row in self.routes:
            print(row)

    def find_a_route(self):
        if self.routes[0][0] == 1:
            return False

        s = Stack()
        visited = set()

        s.push_item((0, 0))
        visited.add((0, 0))

        while not s.is_empty():
            row, column = s.items[-1]

            if (row, column) == (self.side_length - 1, self.side_length - 1):
                print("path found:")
                print(s.items)
                return True  

            moved = False

            if row - 1 >= 0 and self.routes[row - 1][column] == 0 and (row - 1, column) not in visited:
                s.push_item((row - 1, column))
                visited.add((row - 1, column))
                moved = True

            if not moved and row + 1 < self.side_length and self.routes[row + 1][column] == 0 and (row + 1, column) not in visited:
                s.push_item((row + 1, column))
                visited.add((row + 1, column))
                moved = True

            if not moved and column + 1 < self.side_length and self.routes[row][column + 1] == 0 and (row, column + 1) not in visited:
                s.push_item((row, column + 1))
                visited.add((row, column + 1))
                moved = True

            if not moved and column - 1 >= 0 and self.routes[row][column - 1] == 0 and (row, column - 1) not in visited:
                s.push_item((row, column - 1))
                visited.add((row, column - 1))
                moved = True

            if not moved:
                s.pop_item()

        return False



m = Maze(4)
print(m.create_table())
m.show_table()
print(m.find_a_route())
