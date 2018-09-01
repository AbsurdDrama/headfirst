# 类的继承
def sanitize(time_string):
    """
    统一数据格式：将分钟和秒的分隔符统一为 '.' 点
    :param time_string: 输入时间字符串
    :return: 统一结果后的数据
    """
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string

    (mins, secs) = time_string.split(splitter)
    return mins + '.' + secs


class NameList(list):

    def __init__(self, nl_name):
        list.__init__([])  # 初始化派生类
        self.name = nl_name  # 复制新的舒心


class AthleteList(list):

    def __init__(self, a_name, a_dob=None, a_times=None):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def top3(self):
        return sorted(set([sanitize(t) for t in self]))[0:3]


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        tmp = data.strip().split(',')
        print(tmp)
        return AthleteList(tmp.pop(0), tmp.pop(0), tmp)
    except IOError as error:
        print('File Error' + str(error))
        return None


sarah = get_coach_data('mikey2.txt')

print(sarah.name + "'s fastest times are: " + str(sarah.top3()))
