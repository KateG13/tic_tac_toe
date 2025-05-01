def print_field(field):
    print(" 0 1 2")
    for i, row in enumerate(field):
        print(f"{i} {''.join(row)}")

def check_winner(field):
    lines = []
    for i in range(3):
        lines.append(field[i])
        lines.append([field[0][i], field[1][i], field[2][i]])
        lines.append([field[0][0], field[1][1], field[2][2]])
        lines.append([field[0][2], field[1][1], field[2][0]])

        for line in lines:
            if line == ["X"] * 3:
                return "X"
            if line == ["O"] * 3:
                return "O"

        return None

def is_draw(field):
    return all(cell != "-" for row in field for cell in row)

def valid_move(field, x, y):
    return 0 <= x < 3 and 0 <= y < 3 and field[x][y] == "-"

def play_game():
    field = [["-" for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_field(field)
        print(f"Ход игрока {current_player}")

        try:
            x = int(input("Введите номер строки(0, 1 или 2): "))
            y = int(input("Введите номер столбца(0, 1 или 2): "))
        except ValueError:
            print("Введите числа.")
            continue

        if not (0 <= x <= 2 and 0 <= y <= 2):
            print("Координаты вне диапазона")
            continue

        if field[x][y] != "-":
            print("Клетка уже занята")
            continue
        field[x][y] = current_player

        winner = check_winner(field)
        if winner:
            print_field(field)
            print(f"Игрок{winner} победил!")
            break

        if is_draw(field):
            print_field(field)
            print("Ничья!")
            break

        current_player = "O" if current_player == "X" else "X"
if __name__ == "__main__":
    play_game()         