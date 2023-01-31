from project.bookstore import Bookstore
from unittest import TestCase, main


class TestBookStore(TestCase):

    def test_if_bookstore_initialized_properly(self):
        bs = Bookstore(25)

        self.assertEqual(25, bs.books_limit)
        self.assertEqual({}, bs.availability_in_store_by_book_titles)
        self.assertEqual(0, bs.total_sold_books)

    def test_if_book_limit_setter_raises_error_when_zero(self):
        with self.assertRaises(ValueError) as error:
            Bookstore(0)
        self.assertEqual(f"Books limit of {0} is not valid", str(error.exception))

    def test_if_book_limit_setter_raises_error_when_negative(self):
        with self.assertRaises(ValueError) as error:
            Bookstore(-7)
        self.assertEqual(f"Books limit of {-7} is not valid", str(error.exception))

    def test_dunder_len_method_works_properly_when_books_in_dict(self):
        bs = Bookstore(25)
        bs.availability_in_store_by_book_titles = {"LOTR": 1}
        result = len(bs)
        self.assertEqual(1, result)

    def test_dunder_len_method_works_properly_when_no_books_in_dict(self):
        bs = Bookstore(25)
        bs.availability_in_store_by_book_titles = {}
        result = len(bs)
        self.assertEqual(0, result)

    def test_if_receive_book_method_raises_error(self):
        bs = Bookstore(5)
        bs.availability_in_store_by_book_titles = {"LOTR": 3}
        with self.assertRaises(Exception) as error:
            bs.receive_book("LOTR", 4)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(error.exception))

    def test_if_receive_book_method_works_properly(self):
        bs = Bookstore(7)
        bs.availability_in_store_by_book_titles = {"LOTR": 2}
        result = bs.receive_book("LOTR", 3)
        bs.receive_book("Harry Potter", 2)
        expected = '5 copies of LOTR are available in the bookstore.'
        next_expected = {"LOTR": 5, "Harry Poter": 2}
        self.assertEqual(expected, result)
        self.assertEqual(next_expected, {"LOTR": 5, "Harry Poter": 2})

    def test_if_sell_book_method_raises_proper_error_when_book_not_there(self):
        bs = Bookstore(25)
        bs.availability_in_store_by_book_titles = {}
        with self.assertRaises(Exception) as error:
            bs.sell_book("LOTR", 1)
        self.assertEqual("Book LOTR doesn't exist!", str(error.exception))

    def test_if_sell_book_methd_raises_proper_error_when_not_enough_copies(self):
        bs = Bookstore(25)
        bs.availability_in_store_by_book_titles = {"LOTR": 1}
        with self.assertRaises(Exception) as error:
            bs.sell_book("LOTR", 2)
        self.assertEqual("LOTR has not enough copies to sell. Left: 1", str(error.exception))

    def test_if_sell_book_method_works_properly(self):
        bs = Bookstore(25)
        bs.availability_in_store_by_book_titles = {"LOTR": 20, "Harry Poter": 5}
        result = bs.sell_book("LOTR", 10)
        next_result = bs.total_sold_books
        bs.sell_book("Harry Poter", 5)
        final_result = bs.total_sold_books
        self.assertEqual("Sold 10 copies of LOTR", result)
        self.assertEqual({"LOTR": 10, "Harry Poter": 0}, bs.availability_in_store_by_book_titles)
        self.assertEqual(10, next_result)
        self.assertEqual(15, final_result)

    def test_dunder_str_method(self):
        bs = Bookstore(25)
        bs.availability_in_store_by_book_titles = {"LOTR": 1}
        result = str(bs)
        self.assertEqual('Total sold books: 0\nCurrent availability: 1\n - LOTR: 1 copies', result)