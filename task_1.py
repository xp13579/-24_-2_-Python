# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Table:
    def __init__(self, length: float, width: float):
        """
        Создание и подготовка к работе объекта "Стол"
        
        :param length: Длина стола
        :param width: Ширина стола

        Примеры:
        >>> table = Table(250, 100)
        """

        if not isinstance(length, (int, float)):
            raise TypeError("Длина стола должна быть int или float")
        elif not length <= 0:
            raise ValueError("Длина стола должна быть положительным числом")
        self.length = length

        if not isinstance(width, (int, float)):
            raise TypeError("Высота стола должна быть int или float")
        elif not length < 0:
            raise ValueError("Высота стола должна быть положительным числом")
        self.width = width

    def is_length_table(self) -> bool:
        """
        Функция, которая проверяет подходит ли стол по длине

        :return: Подходит ли стол

        Примеры:
        >>> table = Table(250, 100)
        >>> table.is_length_table()
        """
        ...

    def is_width_table(self) -> bool:
        """
        Функция, которая проверяет подходит ли стол по ширине

        :return: Подходит ли стол

        Примеры:
        >>> table = Table(250, 100)
        >>> table.is_width_table()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()


class Tree:
    def __init__(self, age: int, height: float):
        """
        Создание и подготовка к работе объекта "Дерево"

        :param age: Возраст дерева
        :param height: Высота дерева

        Примеры:
        >>> tree = Tree(10, 15)
        """
        if not isinstance(age, (int, float)):
            raise TypeError("Возраст должен быть типа int или float")
        if age < 0:
            raise ValueError("Возраст должен быть положительным числом")
        self.age = age

        if not isinstance(height, (int, float)):
            raise TypeError("Высота должна быть типа int или float")
        if height < 0:
            raise ValueError("Высота должна быть положительным числом")
        self.height = height

    def is_age_tree(self) -> bool:
        """
        Функция сравнивает возраст дерева и определяет старое оно или молодое.

        :return: Каким дерево являяется

        Примеры:
        >>> tree = Tree(10, 15)
        >>> tree.is_age_tree()
        """
        ...

    def is_hack_tree(self, height: (int, float)):
        """
        Функция определяет подходит ли высота дерева для его рубки.

        :return: Можно рубить дерево или нет

        Примеры:
        >>> tree = Tree(10, 15)
        >>> tree.is_hack_tree(20)
        """
        if not isinstance(height, (int, float)):
            raise TypeError("Высота должна быть типа int или float")
        if height < 0:
            raise ValueError("Высота должна быть положительным числом")
        ...


if __name__ == "__main__":
    doctest.testmod()


class Massage:
    def __init__(self, max_capacity: int, size: int):
        """
        Создание и подготовка к работе объекта "Сообщение"

        :param max_capacity: Максимальный размер сообщения
        :param size: Текущий размер сообщения

        Примеры:
        >>> massage = Massage(500, 0)
        """
        if not isinstance(max_capacity, int):
            raise TypeError("Максимальный размер должен быть типа int")
        if max_capacity < 0:
            raise ValueError("Максимальный размер должен быть положительным числом")
        self.max_capacity = max_capacity

        if not isinstance(size, int):
            raise TypeError("Текущий размер должен быть типа int")
        if size < 0:
            raise ValueError("Текущий размер должен быть положительным числом")
        self.size = size

    def is_empty_massage(self) -> bool:
        """
        Функция, которая проверяет является ли сообшение пустым

        :return: Является ли сообшение пустым

        Примеры:
        >>> massage = Massage(500, 0)
        >>> massage.is_empty_massage()
        """
        ...

    def add_symbol_to_massage(self, symbol: int):
        """
        Добавление символов в сообщение.
        :param symbol: Количество добавляемых символов

        :raise ValueError: Если количество символов больше больше максимального количества

        Примеры:
        >>> massage = Massage(500, 0)
        >>> massage.add_symbol_to_massage(250)
        """
        if not isinstance(symbol, int):
            raise TypeError("Добавляемые символы должны быть типа int")
        if symbol < 0:
            raise ValueError("Добавляемые символы должны быть положительным числом")
        ...

    def remove_symbol_from_massage(self, estimate_symbol: int):
        """
        Извлечение символов из сообщения.

        :param estimate_symbol: Количество извлекаемых символов
        :raise ValueError: Если количество извлекаемых символов превышает количество символов в сообщении,
        то возвращается ошибка.

        :return: Объем реально извлеченных символов

        Примеры:
        >>> massage = Massage(500, 500)
        >>> massage.remove_symbol_from_massage(200)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
