# game.py
# Основной исполняемый файл.
# Код в функции main() выполняется только при запуске файла напрямую, а не при импорте.

from gameparts.parts import Board

def main():
    # Демонстрация игрового процесса
    game = Board()
    game.display()
    game.make_move(1, 1, 'X')
    print('Ход сделан!')
    game.display()

# Запуск только при прямом запуске, не при импорте
if __name__ == '__main__':
    main()
