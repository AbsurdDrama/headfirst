# -*- coding: UTF-8 -*-


class Stack(object):
    __slots__ = '__items'

    def __init__(self):
        self.__items = []

    def is_empty(self):
        """
        判断 stack 是否为空
        :return: 布尔 True or False
        """
        return self.__items == []

    def peek(self):
        """
        取出栈顶元素
        :return: 返回栈顶元素
        """
        # TODO: IndexError Test
        return self.__items[len(self.__items) - 1]

    def push(self, item):
        """
        元素入栈
        list 对象中,栈顶 = len(list) - 1, 栈底 = 0
        :return: 新元素入栈插入到 item 末端
        """
        self.__items.append(item)

    def pop(self):
        """
        出栈 将栈顶元素出栈
        :return: 返回栈顶元素
        """
        return self.__items.pop(len(self.__items) - 1)

    def all(self):
        """
        返回栈所有元素
        :return: 返回 __items 属性
        """
        return self.__items
