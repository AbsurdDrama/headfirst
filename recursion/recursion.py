def print_lol(this_list, indent=False, level=0):
    """
    解析嵌套数组数据
    :param indent: 是否使用换行缩进
    :param this_list: 任意嵌套的列表元素
    :param level: 嵌套列表之间是否用TAB隔开
    :return: 打印出嵌套的数据列表
    """
    for each_element in this_list:
        if isinstance(each_element, list):
            print_lol(each_element, indent, level + 1)
            # 递归函数参数变化同时注意内部调用的变化
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end='')
                    # 缩进使用tab键
            print(each_element)


recursion = ["a", "a1", ["b", "b1", ["c"]], ["d", "E"], "P"]

if __name__ == "__main__":

    print_lol(this_list=recursion, indent=True, level=0)