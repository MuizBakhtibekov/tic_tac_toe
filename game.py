# game.py

from gameparts import Board
from gameparts.exceptions import CellOccupiedError, FieldIndexError


def save_result(result):
    with open('results.txt', 'a', encoding='utf-8') as file:
        file.write(result + '\n')

    # Дополнительно сохраняем результат в отдельный файл
    with open('last_result.txt', 'w', encoding='utf-8') as f:
        f.write(result)


def main():
    game = Board()
    # Первыми ходят крестики.
    current_player = 'X'
    running = True
    game.display()

    while running:

        print(f'Ходит {current_player}')

        while True:
            try:
                row = int(input('Введите номер строки: '))
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError
                column = int(input('Введите номер столбца: '))
                if column < 0 or column >= game.field_size:
                    raise FieldIndexError
                if game.board[row][column] != ' ':
                    raise CellOccupiedError
            except FieldIndexError:
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}.'
                )
                print('Введите значения для строки и столбца заново.')
                continue
            except CellOccupiedError:
                print('Ячейка занята.')
                print('Введите другие координаты.')
                continue
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print('Введите значения для строки и столбца заново.')
                continue
            except Exception as e:
                print(f'Возникла ошибка: {e}')
            else:
                break

        game.make_move(row, column, current_player)
        game.display()
        if game.check_winner(current_player):
            # Сформировать строку.
            result = f'Победили {current_player}.'
            # Вывести строку на печать.
            print(result)
            # Добавить строку в файл.
            save_result(result)
            running = False
        elif game.is_board_full():
            # Сформировать строку.
            result = 'Ничья!'
            # Вывести строку на печать.
            print(result)
            # Добавить строку в файл.
            save_result(result)
            running = False

        current_player = 'O' if current_player == 'X' else 'X'



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
