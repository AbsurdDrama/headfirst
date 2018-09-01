# -*- coding: UTF-8 -*-


class Queue(object):
    __slots__ = '__items'

    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def len(self):
        return len(self.__items)

    def insert(self, item):
        return self.__items.insert(0, item)

    def pop(self):
        return self.__items.pop()

