# рисуем игровое поле
def draw_board(board):
    print("{}|{}|{}".format(board[0], board[1], board[2]))
    print("{}|{}|{}".format(board[3], board[4], board[5]))
    print("{}|{}|{}".format(board[6], board[7], board[8]))

# определяем буквы за игроками
def input_player_letter():
    # создаем цикл
    while True:
        # спрашиваем игрока
        print('Играем за X или O?')
        letter = input().upper()
        if letter == 'X':
            return ['X', 'O']
        elif letter == 'O':
            return ['O', 'X']
    print("Пользователь выбрал: ", letter)

# определяем кто ходит первый
def choose_first():
    import random
    if random.randint(0, 1) == 0:
        return 'Игрок 1'
    else:
        return 'Игрок 2'

# определяем возможность хода
def is_space_free(board, index):
    return board[index] == ' '

# определяем ход игрока
def get_players_move(board):
    # цикл
    while True:
        # запрос на позицию поля
        print('Куда ходим выбрать, ячейку от 1 до 9?', turn)
        move = input()
        # проверяем что введена цифра
        if move.isdigit():
            move = int(move) - 1
            if move >= 0 and move <= 8 and is_space_free(board, move):
                return move

# присваеваем букву к позиции поля
def insert_letter_at(letter, board, pos):
    board[pos] = letter

# проверка на полное игровое поле, ничью
def is_board_full(board):
    for i in range(0, 9):
        if is_space_free(board, i):
            return False
    return True

# определяем выйгрышные комбинации
def is_winner(l, b):
    return (b[0] == l and b[1] == l and b[2] == l) or (b[3] == l and b[4] == l and b[5] == l) or \
            (b[6] == l and b[7] == l and b[8] == l) or (b[0] == l and b[3] == l and b[6] == l) or \
            (b[1] == l and b[4] == l and b[7] == l) or (b[2] == l and b[5] == l and b[8] == l) or \
            (b[0] == l and b[4] == l and b[8] == l) or (b[2] == l and b[4] == l and b[6] == l)

# Игра!

print('Играем в крестики-нолики?!')

while True:
    # сбрасываем параметры поля
    board = [' '] * 9
    p_1_letter, p_2_letter = input_player_letter()
    turn = choose_first()
    print(turn + ' Ходит первым.')
    game_is_playing = True

    while game_is_playing:
        if turn == 'Игрок 1':
            # ход игрока 1
            draw_board(board)
            move = get_players_move(board)
            insert_letter_at(p_1_letter, board, move)

            if is_winner(p_1_letter, board):
                draw_board(board)
                print('Игрок 1 победил!')
                game_is_playing = False
            else:
                if is_board_full(board):
                    draw_board(board)
                    print('Ничья!')
                    break
                else:
                    turn = 'Игрок 2'
        else:
            # Ход второго игрока
            turn == 'Игрок 2'
            draw_board(board)
            move = get_players_move(board)
            insert_letter_at(p_2_letter, board, move)


            if is_winner(p_2_letter, board):
                draw_board(board)
                print('Игрок 2 победил!')
                game_is_playing = False
            else:
                if is_board_full(board):
                    draw_board(board)
                    print('Ничья!')
                    break
                else:
                    turn = 'Игрок 1'

    print('Хотите повторить? (yes or no)')
    if not input().lower().startswith('y'):
        break