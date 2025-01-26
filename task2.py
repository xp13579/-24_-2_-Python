BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    """Класс для представления книги"""

    def __init__(self, id_: int, name: str, pages: int):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        """Возвращает строку формата: Книга "название_книги"."""
        return f'Книга "{self.name}"'

    def __repr__(self):
        """
        Возвращает строку, по которой можно инициализировать точно такой же экземпляр.
        Пример: Book(id_=1, name='test_name_1', pages=200)
        """
        return f"Book(id_={self.id}, name={self.name!r}, pages={self.pages})"


# TODO написать класс Library
class Library:
    """Класс для представления библиотеки"""

    def __init__(self, books=None):
        """
        Инициализирует библиотеку.
        :param books: Список книг. Если не указан, по умолчанию пустой список.
        """
        self.books = books if books is not None else []

    def get_next_book_id(self) -> int:
        """
        Возвращает идентификатор для добавления новой книги в библиотеку.
        Если книг нет, возвращает 1.
        """
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Возвращает индекс книги по её идентификатору.
        Если книги с таким id нет, вызывает ValueError.
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
