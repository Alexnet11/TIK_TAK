
field = [[" "]*3 for i in range(3)]

def greetings():
    print("------------------ ")
    print(" Приветсвуем Вас   ")
    print("     в игре        ")
    print(" крестики -нолики  ")
    print("------------------ ")
    print(" формат ввода: х,y ")
    print(" x - номер строки  ")
    print(" Y - номер столбца ")

def show():
    print()
    print("    | 0 | 1 | 2 | ")
    print(" -----------------")
    for i, row in enumerate(field):
        rows_str = f"  {i} | {' | '.join(row)} | "
        print(rows_str)
        print(" --------------- ")
    print()

def ask():
    while True:
        cords = input(        "Ваш ход: " ).split()

        if len(cords) != 2:
            print(" ВВЕДИТЕ 2 КООРДИНАТЫ! ")
            continue

        x, y = cords

        if not(x.isdigit()) or not(y.isdigit()):
            print(" ВВЕДИТЕ ЧИСЛО ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" КООРДИНАТЫ В НЕ ДИОПОЗОНА ")
            continue

        if field[x][y] != " ":
            print(" КЛЕТКА ЗАНЯТА ")
            continue

        return x, y

def check():
    win_cord = [((0,0),(0,1),(0,2)), ((1,0),(1,1),(1,2)), ((2,0), (2,1),(2,2)), ((0,0),(1,0),(2,0)), ((0,1), (1,1), (2,1)), ((0,2), (1,2), (2,2)), ((0,0), (1,1), (2,2)), ((0,2),(1,1),(2,0)) ]

    for cord in win_cord:
        a = cord[0]
        b = cord[1]
        c = cord[2]

        if field[a[0]][a[1]] == field[b[0]][b[1]] == field[c[0]][c[1]] != " ":
            print(f"Выйграл {field[a[0]][a[1]]}!")
            return True
    return False


greetings()
num = 0
while True:
    num += 1


    show()

    if num % 2 == 1:
        print(" Ход Х ")
    else:
        print(" Ходит O ")

    x, y = ask()

    if num % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "O"

    if check():
        break

    if num == 9:
        print(" НИЧЬЯ ")
        break

