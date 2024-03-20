#!/usr/bin/env python3

from book import Book

import io
import sys

class TestBook:
    def test_has_title_author_price_pages(self):
        '''has the title, author, price, and pages passed into __init__, and values can be set to new instance.'''
        book = Book("And Then There Were None", "Agatha Christie", 10.99, 272)
        assert book.get_title() == "And Then There Were None"
        assert book.get_author() == "Agatha Christie"
        assert book.get_price() == 10.99
        assert book.get_pages() == 272


    
    def test_requires_int_page_count(self):
        '''prints "page_count must be an integer" if page_count is not an integer.'''
        with pytest.raises(TypeError, match="page_count must be an integer"):
            book = Book("And Then There Were None", "Agatha Christie", 10.99, "272")

    def test_can_turn_page(self):
        '''outputs "Flipping the page...wow, you read fast!" when method turn_page() is called'''
        book = Book("The World According to Garp", 69)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        book.turn_page()
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Flipping the page...wow, you read fast!\n")
