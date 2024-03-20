#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, model, size, color, price):
        self.brand = brand
        self.model = model
        self.size = size
        self.color = color
        self.price = price

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_size(self):
        return self.size

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price

    def __str__(self):
        return f"{self.brand} {self.model} - {self.color}"
