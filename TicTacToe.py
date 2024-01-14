# крестики-нолики

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def draw_board():
    "'Создаёт игровое поле'"
    for i in range(len(board)):
        print(f' {board[i]} ', end='')
        if (i + 1) % 3 == 0 and i != 9:
            print("\n---+---+---")
        elif i != 9:
            print('|', end='')
    print()

def game_step(index, char):
    "'Выполняет ход'"
    if (index > 9 or index < 1 or board[int(index)-1] in ('X', 'O')):
        return False

    board[int(index)-1] = char
    return True

def check_win():
    "'Выполняет проверку выйгрыша'"
    win = False
    win_combination = (
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    )

    for pos in win_combination:
        if (board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]]):
            win = board[pos[0]]
    return win

def print_hart():
    "'Рисует сердце'"
    for i in range(5):
        for j in range(7):
            if (i == 0 and j != 0 and j != 3 and j != 6) or (i == 1 and j != 1 and j != 2 and j != 4 and j != 5) or (
                    i == 2 and j != 0 and j != 2 and j != 3 and j != 4 and j != 6) or (
                    i == 3 and j != 0 and j != 1 and j != 3 and j != 5 and j != 6) or (
                    i == 4 and j != 0 and j != 1 and j != 2 and j != 4 and j != 5 and j != 6):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def start_game():
    # текущий игрок
    current_player = 'X'
    # номер хода
    step = 1
    draw_board()

    while (step < 10) and (check_win() == False):
        index = input("Игрок " + current_player + ", введите номер поля (0-выход):")

        if (index == "0"):
            break

        if (game_step(int(index), current_player)):
            print('Вы сделали ход')

            if (current_player == 'X'):
                current_player = 'O'
            else:
                current_player = 'X'

            draw_board()

            step += 1
        else:
            print("Неверный номер поля! Повторите!")
    if (step == 10):
        print("Игра окончена! Ничья!")
    else:
        print_hart()
        print('Выиграл игрок ' + check_win())


print("Преветсвуем в игре Крестики-нолики!")

start_game()

