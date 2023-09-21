#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Maisha Taranum
Class: CS 521 - Summer 2
Date: 08/15/2023
shop_class.py that defines a user-defined class Shop with required structures
"""

class Shop:
    def __init__(self, shop_type, area, date, prices, store_hours):
        self.shop_type = shop_type
        self.area = area
        self.date = date
        self.prices = prices
        self.store_hours = store_hours
    def get_store_hours(self):
        return self.store_hours
    # Private class attribute
    _private_attr = "This is a private attribute"

    # Public class attributes
    public_attr1 = "Public attribute 1"
    public_attr2 = "Public attribute 2"

    @classmethod
    def public_class_method1(cls, arg1, arg2):
        return f"Public class method 1 called with arguments: {arg1}, {arg2}"

    @classmethod
    def public_class_method2(cls, arg1, arg2):
        return f"Public class method 2 called with arguments: {arg1}, {arg2}"

    def private_instance_method(self):
        return "Private instance method called"

    def public_instance_method(self):
        return "Public instance method called"

    @classmethod
    def init_class_method(cls, arg):
        return f"Init class method called with argument: {arg}"

    def __str__(self):
        return f"Shop({self.shop_type}, {self.area}, {self.date})"

    @staticmethod
    def magic_method():
        return "This is a magic method"

# This code won't be executed if the module is imported
if __name__ == "__main__":
    shop = Shop("shoes", "downtown", "2023-06-25", [50, 60, 70], \
                "10:00 AM - 8:00 PM")
    print(shop.private_instance_method())
    print(shop.public_instance_method())
    print(Shop.public_class_method1("arg1_value", "arg2_value"))
    print(Shop.public_class_method2("arg1_value", "arg2_value"))
    print(Shop.init_class_method("arg_value"))
    print(shop)
    print(Shop.magic_method())