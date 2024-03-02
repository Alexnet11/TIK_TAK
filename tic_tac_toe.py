
field = 3  # размер игрового поля

playing_field = [1,2,3,4,5,6,7,8,9] # ячейки игрового поля

def draw_field():
    '''Выводим игровое поле'''
    print("_" * 4 * field)
    for i in range(field):
        print((' ' * 3 + "|" )*3)
        print('', playing_field[i*3], "|", playing_field[1+i*3], "|", playing_field[ 2 + i * 3], "|")
        print("_" * 4 * field)
    pass

def make_move(index, char):
    '''Делаем ход'''
    if (index > 9 or index < 1 or playing_field[index-1] in ('X', "O")):
        return False

    playing_field[index-1] = char
    return True

def checking():
    '''Проверяем ход'''
    win = False
    win_comb = (
        (0,1,2), (3,4,5), (6,7,8), # горизонтальные
        (0,3,6), (1,4,7), (2,5,8), # верикальные
        (0,4,8), (2,4,6,)
    )
    for pos in win_comb:
        if (playing_field[pos[0]] == playing_field[pos[1]] and playing_field[pos[1]] == playing_field[pos[2]] ):
            win = playing_field[pos[0]]
    return win

def start_game():
    # текущий игрок
    current_player = "Х"
    # номер шага
    move = 1
    draw_field()

    while (move < 9) and (checking() == False):
        index = input('Ход игрока' + current_player + ".Введите номер поля:")

        #if index == 0:
        #    index = 1

        if (index == "0"):
            break

        # получилость сделать шаг
        if make_move(int(index), current_player):
            print("Удачный ход")

            if (current_player == "X"):
                current_player = "O"
            else:
                current_player ="X"

            draw_field()
            # увеличиваем номер хода
            move += 1
        else:
            print("Не коректный номер.Повторите ход")

    print("Выйграл" + checking())

print("Начало игры Крестики - нолики!")
start_game()


