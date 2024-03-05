class Book:  # создаем "основной" класс
    page_material = "paper"  # общий атрибут, будет доступен и во вложенном классе
    availability_of_text = True  # общий атрибут, будет доступен и во вложенном классе

    """
    Создаем индивидуальные атрибуты доступные только для класса Book (инициализируем атрибуты класса Book)
    """
    def __init__(self, title, author, number_of_pages, isbn, flag_whether_the_book_or_not):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self._isbn = isbn
        self.flag_whether_the_book_or_not = flag_whether_the_book_or_not

    """
    Создаем функцию которая выводит набор атрибутов при выполнении условия
    if self.flag_whether_the_book_or_not == True
    """

    def print_ditails(self):
        if self.flag_whether_the_book_or_not:  # аналог if self.flag_whether_the_book_or_not == True
            book_name = (f"Title: {self.title}, author: {self.author}, pages: {self.number_of_pages}, "
                         f"matirial: {self.page_material}, reserved")
        else:
            book_name = (f"Title: {self.title}, author: {self.author}, pages: {self.number_of_pages}, "
                         f"matirial: {self.page_material}")
        return book_name


book_1 = Book("Lord of the rings", "J. R. R. Tolkien", 1000,
              22250, True)
book_2 = Book("Beowulf: The Monsters and the Critics", "J. R. R. Tolkien_2", 1020,
              22251, False)
book_3 = Book("On Fairy-Stories", "J. R. R. Tolkien_3", 700,
              22252, False)
book_4 = Book("The Hobbit", "J. R. R. Tolkien_4", 600,
              22253, False)
book_5 = Book("The Silmarillion", "J. R. R. Tolkien_5", 579,
              22254, False)


class SchoolBook(Book):  # создаем класс вложенный в класс Book и определяем его атрибуты
    subject = "предмет (типа математика, история, география)"
    for_class = "школьный класс, для которого этот учебник"
    tasks = "True/False"

    """
    Инициализируем атрибуты для нового класса, первый init содержит атрибуты доступные классу SchoolBook
    Вторая строка описывает класс из которого импортируем часть атрибутов из класса Book
    """

    def __init__(self, title, author, number_of_pages, isbn, flag_whether_the_book_or_not, subject, for_class, tasks):
        super().__init__(title, author, number_of_pages, isbn, flag_whether_the_book_or_not)
        self.subject = subject
        self.for_class = for_class
        self.tasks = tasks

    """
    Создаем функцию которая выводит набор атрибутов при выполнении условия
    if self.flag_whether_the_book_or_not == True
    """

    def print_ditails(self):
        if self.flag_whether_the_book_or_not:  # аналог if self.flag_whether_the_book_or_not == True
            book_name = (
                f"Title: {self.title}, author: {self.author}, pages: {self.number_of_pages}, subject: {self.subject}, "
                f"class: {self.for_class}, reserved")
        else:
            book_name = (
                f"Title: {self.title}, author: {self.author}, pages: {self.number_of_pages}, subject: {self.subject}, "
                f"class: {self.for_class}")
        return book_name


school_book_1 = SchoolBook("Belarusian history", "Pogankina A.A", 200, 33445,
                           False, "History", 11, True)

school_book_2 = SchoolBook("Biology 11", "Hvoin A.G", 223, 33446,
                           True, "Biology", 8, False)

print(Book.print_ditails(book_1), Book.print_ditails(book_2), Book.print_ditails(book_3), Book.print_ditails(book_4),
      Book.print_ditails(book_5), SchoolBook.print_ditails(school_book_1), SchoolBook.print_ditails(school_book_2),
      sep="\n")
