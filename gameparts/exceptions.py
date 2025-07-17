# gameparts/exceptions.py
"""Модуль содержит пользовательские исключения для игры 'Крестики-нолики'."""

class FieldIndexError(IndexError):
    """Выбрасывается, если выбрано значение вне поля."""

    def __init__(self, message='Введено значение за границами игрового поля!'):
        super().__init__(message)  # ✅ Больше НИКАКИХ двоеточий здесь

class CellOccupiedError(Exception):
    def __init__(
            self,
            message='Попытка изменить занятую ячейку'
        ):

        super().__init__(message)