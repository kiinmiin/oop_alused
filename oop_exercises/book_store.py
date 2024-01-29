"""Book store."""


class Book:
    """Represent book model."""

    def __init__(self, title: str, author: str, price: float, rating: float):
        """
        Class constructor. Each book has title, author and price.

        :param title: book's title
        :param author: book's author
        :param price: book's price
        """
        self.title = title
        self.author = author
        self.price = price
        self.rating = rating
        


class Store(Book):
    """Represent book store model."""

    def __init__(self, name: str, rating: float):
        """
        Class constructor.

        Each book store has name.
        There also should be an overview of all books present in store

        :param name: book store name
        """
        self.name = name
        self.rating = rating
        self.books = []
        pass

    def can_add_book(self, book) -> bool:
        """
        Check if book can be added.

        It is possible to add book to book store if:
        1. The book with the same author and title is not yet present in this book store
        2. book's own rating is >= than store's rating
        :return: bool
        """
        for store_book in self.books:
            if book.title == store_book.title and book.author == store_book.author:
                return False
        if book not in self.books and book.rating >= self.rating:
            return True
        else:
            return False

    def add_book(self, book: Book):
        """
        Add new book to book store if possible.

        :param book: Book
        Function does not return anything
        """
        if self.can_add_book(book):
            self.books.append(book)


    def can_remove_book(self, book: Book) -> bool:
        """
        Check if book can be removed from store.

        Book can be successfully removed if it is actually present in store

        :return: bool
        """
        if book in self.books:
            return True
        else:
            return False

    def remove_book(self, book: Book):
        """
        Remove book from store if possible.

        Function does not return anything
        """
        if self.can_remove_book(book):
            self.books.remove(book)
        pass

    def get_all_books(self) -> list:
        """
        Return a list of all books in current store.

        :return: list of Book objects
        """
        return self.books
        pass

    def get_books_by_price(self) -> list:
        """
        Return a list of books ordered by price (from cheapest).

        :return: list of Book objects
        """
        self.books.sort(key=lambda x: x.price)
        return self.books
        pass

    def get_most_popular_book(self) -> list:
        """
        Return a list of book (books) with the highest rating.

        :return: list of Book objects
        """
        highest_rating = 0
        most_popular_books = []

        for book in self.books:
            if book.rating == highest_rating:
                most_popular_books.append(book)
            elif book.rating > highest_rating:
                highest_rating = book.rating
                most_popular_books = [book]

        return most_popular_books
        pass

store = Store("Apollo", 50)
book1 = Book("War", "Leo Tolstoy", 10.5, 75)
book2 = Book("Peace", "Leo Tolstoy", 5, 99)
book3 = Book("Sun", "Leo Tolstoy", 34, 86)
book4 = Book("Food", "Leo Tolstoy", 11, 44)
book5 = Book("Sea", "Leo Tolstoy", 23, 78)
book6 = Book("Water2", "Leo Tolstoy", 3, 66)
book7 = Book("Water", "Leo Tolstoy", 3, 99)

store.add_book(book1)
store.add_book(book2)
store.add_book(book3)
store.add_book(book4)
store.add_book(book5)
store.add_book(book6)
store.add_book(book7)

print(store.books)

store.remove_book(book3)

print(store.books)


