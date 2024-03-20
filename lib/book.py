#!/usr/bin/env python3

class Book:
    def __init__(self, title, author, price, pages):
        self.title = title
        self.author = author
        self.price = price
        self.pages = pages

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_price(self):
        return self.price

    def get_pages(self):
        return self.pages

    def __str__(self):
        return f"{self.title} by {self.author}"


    
        