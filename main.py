import random


class Robot:

    def __init__(self):
        self.robots_turns = []

    def get_robot_turns(self):
        return self.robots_turns

    def add_robot_turn(self, i, j):
        robot_turns.append(i, j)


class Ship:

    def __init__(self, width):
        self.width = width

    def get_width(self):
        return self.width

    def check(self):
        if self.width == 1:
            print('вы выбрали одинарный корабль!')
        elif self.width == 2:
            print('вы выбрали двойной корабль!')
        elif self.width == 3:
            print('вы выбрали тройной корабль!')
        else:
            print('wrong answer!')

    def validate_ship_position(self, start_point_i, start_point_j, width, horisontal_or_vertical, game_field):
        if start_point_i < 1 or start_point_j < 1 or start_point_i > 6 or start_point_j > 6:
            return False
        if horisontal_or_vertical == 0 and start_point_j + width - 1 > 6:
            return False
        if horisontal_or_vertical == 1 and start_point_i + width - 1 > 6:
            return False

        if horisontal_or_vertical == 0:
            for k in range(start_point_j, start_point_j + self.width):
                if (game_field[start_point_i - 1][k - 1] == 1):
                    return False
        else:
            for k in range(start_point_i, start_point_i + self.width):
                if game_field[k - 1][start_point_j - 1] == 1:
                    return False
        return True

    def position_ship_by_user(self, game_field):
        i = -1
        j = -1
        horisontal_or_vertical = -1

        while not self.validate_ship_position(i, j, self.width, horisontal_or_vertical, game_field):
            i = int(input('первая координата куда хотите поставить начальную точку корабля?'))
            j = int(input('вторая координата куда хотите поставить начальную точку корабля?'))
            if self.width > 1:
                horisontal_or_vertical = int(input('горизонтально(0) или вертикально(1)?'))

        if horisontal_or_vertical == 0:
            for k in range(j, j + self.width):
                game_field[i - 1][k - 1] = 1
        else:
            for k in range(i, i + self.width):
                game_field[k - 1][j - 1] = 1

    def position_ship_by_robot(self, game_field):
        i = -1
        j = -1
        horisontal_or_vertical = -1

        while not self.validate_ship_position(i, j, self.width, horisontal_or_vertical, game_field):
            i = random.randint(0, 6)
            j = random.randint(0, 6)
            if self.width > 1:
                horisontal_or_vertical = random.randint(0, 1)

        if horisontal_or_vertical == 0:
            for k in range(j, j + self.width):
                game_field[i - 1][k - 1] = 1
        else:
            for k in range(i, i + self.width):
                game_field[k - 1][j - 1] = 1


class Game:

    def __init__(self):
        self.game_field = [[0 for i in range(6)] for j in range(6)]
        self.game_field_robot = [[0 for a in range(6)] for b in range(6)]

    def get_game_field(self):
        return self.game_field

    def get_game_field_robot(self):
        return self.game_field_robot

    def attack(self, i, j, game_field):
        if self.game_field[i - 1][j - 1] == 1:
            self.game_field[i - 1][j - 1] = 2
            print('Hit!')
            return True
        elif self.game_field[i-1][j-1] == 'X':
            print("You guessed that one already.")
        else:
            print('Missed!')
            game_field[i-1][j-1] = 'X'
            return False


    def start(self):

        player_succes_count = 0
        robot_succes_count = 0

        valid = False
        while not valid:

            print('ваш ход!')
            i = int(input('куда ударим по i:'))
            print(i)
            j = int(input('куда ударим по j:'))
            print(j)
            if self.attack(i, j, self.game_field):
                player_succes_count += 1

            print("Ходит робот!")
            i = random.randint(0, 6)
            j = random.randint(0, 6)
            if self.attack(i, j, self.game_field_robot):
                robot_succes_count += 1


            if player_succes_count == 11:
                print('Player  is winner!')
                valid = True
            elif robot_succes_count == 11:
                print('Robot  is winner!')
                valid = True

    def draw_board(self):
        print(" Your field")
        print(" |1|2|3|4|5|6|")
        for j in range(0, 6):
            line_str = str(j + 1) + '|'
            for i in range(0, 6):
                line_str = line_str + str(self.game_field[j][i]) + '|'
            print(line_str)

    def draw_board_robot(self):
        print()
        print(" Robot's field")
        print(" |1|2|3|4|5|6|")
        for j in range(0, 6):
            line_str = str(j + 1) + '|'
            for i in range(0, 6):
                line_str = line_str + str(self.game_field_robot[j][i]) + '|'
            print(line_str)


game = Game()
game.draw_board()
game.draw_board_robot()

s = Ship(3)
s.check()
s.position_ship_by_user(game.get_game_field())

for i in range(2):
    s = Ship(2)
    s.check()
    s.position_ship_by_user(game.get_game_field())
for i in range(4):
    s = Ship(1)
    s.check()
    s.position_ship_by_user(game.get_game_field())

s = Ship(3)
s.position_ship_by_robot(game.get_game_field_robot())

for i in range(2):
    s = Ship(2)
    s.position_ship_by_robot(game.get_game_field_robot())
for i in range(5):
    s = Ship(1)
    s.position_ship_by_robot(game.get_game_field_robot())

game.start()

draw_board(game.get_game_field())
draw_board_robot(game.get_game_field_robot())