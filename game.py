from gameparts import Board
import pygame

pygame.init()

CELL_SIZE = 100
BOARD_SIZE = 3
WIDTH = HEIGHT = CELL_SIZE * BOARD_SIZE
LINE_WIDTH = 15
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
X_COLOR = (84, 84, 84)
O_COLOR = (242, 235, 211)
X_WIDTH = 15
O_WIDTH = 15
SPACE = CELL_SIZE // 4

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Крестики-нолики')
screen.fill(BG_COLOR)

def draw_lines():
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(
            screen, LINE_COLOR,
            (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), LINE_WIDTH
        )
        pygame.draw.line(
            screen, LINE_COLOR,
            (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), LINE_WIDTH
        )

def draw_figures(board):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == 'X':
                pygame.draw.line(
                    screen, X_COLOR,
                    (col * CELL_SIZE + SPACE, row * CELL_SIZE + SPACE),
                    (col * CELL_SIZE + CELL_SIZE - SPACE, row * CELL_SIZE + CELL_SIZE - SPACE),
                    X_WIDTH
                )
                pygame.draw.line(
                    screen, X_COLOR,
                    (col * CELL_SIZE + SPACE, row * CELL_SIZE + CELL_SIZE - SPACE),
                    (col * CELL_SIZE + CELL_SIZE - SPACE, row * CELL_SIZE + SPACE),
                    X_WIDTH
                )
            elif board[row][col] == 'O':
                pygame.draw.circle(
                    screen, O_COLOR,
                    (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2),
                    CELL_SIZE // 2 - SPACE, O_WIDTH
                )

def save_result(result):
    with open('results.txt', 'a', encoding='utf-8') as file:
        file.write(result + '\n')
    with open('last_result.txt', 'w', encoding='utf-8') as f:
        f.write(result)

def main():
    game = Board()
    current_player = 'X'
    running = True
    game_over = False

    draw_lines()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouse_x = event.pos[0]
                mouse_y = event.pos[1]

                col = mouse_x // CELL_SIZE
                row = mouse_y // CELL_SIZE

                if game.board[row][col] == ' ':
                    game.make_move(row, col, current_player)

                    if game.check_winner(current_player):
                        save_result(f'Победил {current_player}')
                        game_over = True
                    elif game.is_board_full():
                        save_result('Ничья!')
                        game_over = True
                    else:
                        current_player = 'O' if current_player == 'X' else 'X'

        draw_figures(game.board)
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()

# Подробный разбор кода

# Цикл while True — это бесконечный цикл, который будет работать до тех пор, пока инструкция break не прервёт его. Если введённые значения соответствуют условиям, то цикл завершается и управление программой передаётся следующим строкам кода.
# Блоки try и except:
# Программа пытается выполнить операции в блоке try.
# Если возникает исключение, управление передаётся блоку except.
# Ввод и проверка номера строки (row):
# Пользователю предлагается ввести номер строки. Это значение преобразуется в целое число.
# Если введённое число row меньше 0 или больше или равно game.field_size, выбрасывается собственное исключение FieldIndexError.
# Ввод и проверка номера столбца (column):
# Пользователю предлагается ввести номер столбца. Это значение также преобразуется в целое число.
# Далее проверяется, находится ли значение column в допустимом диапазоне, и если нет, то выбрасывается исключение FieldIndexError.
# Обработка исключения FieldIndexError:
# Если возникает исключение FieldIndexError (например, из-за некорректного ввода), код выводит сообщение об ошибке, указывая на недопустимость введённых значений.
# После вывода сообщения с помощью continue цикл начинает свою работу сначала, предоставляя пользователю ещё одну попытку ввести данные.
# Блок else:
# Если в блоке try не возникло исключений, выполнение доходит до блока else, и цикл прерывается с помощью break. Это означает, что введённые значения прошли все проверки и могут быть использованы в дальнейшем.
