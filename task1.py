class SoundMixin:
    """
    Миксин для добавления функционала издания звука.
    """
    def make_sound(self, sound: str) -> str:
        return sound


class Animal:
    """
    Базовый класс, описывающий обобщённые характеристики животных.
    """

    def __init__(self, name: str, age: int):
        """
        Инициализация объекта животного.

        :param name: Имя животного.
        :param age: Возраст животного.
        """
        self.name = name
        self.age = age
        self._health_status = "Healthy"  # Непубличный атрибут, т.к. доступ к состоянию здоровья должен быть ограничен

    def __str__(self, extra_info: str = "") -> str:
        """
        Универсальный метод строкового представления с возможностью добавления дополнительной информации.

        :param extra_info: Дополнительная информация о животном.
        """
        base_info = f"Животное: {self.name}, Возраст: {self.age} лет"
        return f"{base_info}, {extra_info}" if extra_info else base_info

    def __repr__(self) -> str:
        return f"Animal(name={self.name!r}, age={self.age!r})"

    def get_health_status(self) -> str:
        """
        Метод для получения состояния здоровья животного.
        """
        return self._health_status


class Mammal(Animal, SoundMixin):
    """
    Дочерний класс, представляющий млекопитающих.
    """

    def __init__(self, name: str, age: int, fur_color: str):
        """
        Расширяем конструктор родительского класса добавлением цвета шерсти.

        :param name: Имя животного.
        :param age: Возраст животного.
        :param fur_color: Цвет шерсти.
        """
        super().__init__(name, age)
        self.fur_color = fur_color

    def __str__(self) -> str:
        """
        Используем общий метод с дополнительной информацией.
        """
        return super().__str__(f"Цвет шерсти: {self.fur_color}")


class Bird(Animal, SoundMixin):
    """
    Дочерний класс, представляющий птиц.
    """

    def __init__(self, name: str, age: int, wing_span: float):
        """
        Расширяем конструктор родительского класса добавлением размаха крыльев.

        :param name: Имя птицы.
        :param age: Возраст птицы.
        :param wing_span: Размах крыльев (в метрах).
        """
        super().__init__(name, age)
        self.wing_span = wing_span

    def __str__(self) -> str:
        """
        Используем общий метод с дополнительной информацией.
        """
        return super().__str__(f"Размах крыльев: {self.wing_span} м")


if __name__ == "__main__":
    animal = Animal("Неизвестное", 5)
    mammal = Mammal("Лев", 4, "золотистая")
    bird = Bird("Орел", 3, 2.1)

    print(animal)
    print(animal.get_health_status())

    print(mammal)
    print(mammal.make_sound("Рык"))

    print(bird)
    print(bird.make_sound("Чириканье"))
