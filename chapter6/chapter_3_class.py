# Athlete Class Process Data


"""封装类实现"""


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


class Athlete(object):

    def __init__(self, a_name, a_dob=None, a_times=None):
        if a_times is None:
            a_times = []
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

    def top3(self):
        return sorted(set([sanitize(t) for t in self.times]))[0:3]

    def add_time(self, new_time):
        self.times.append(new_time)

    def add_times(self, new_times=[]):
        self.times.extend(new_times)


# 通过代码实例化对象
t_athlete = Athlete('t_athlete')
t_athlete.add_time('1.88')
t_athlete.add_times(['1.99', '1.82', '2.13'])
print(t_athlete.top3())


# 函数调用过程中实例化 Athlete 类对象
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
            tmp = data.strip().split(',')
            return Athlete(tmp.pop(0), tmp.pop(0), tmp)
    except IOError as error:
        print('File Error' + str(error))
        return None


james = get_coach_data('james2.txt')
julie = get_coach_data('julie2.txt')
mikey = get_coach_data('mikey2.txt')
sarah = get_coach_data('sarah2.txt')

james.add_time('1.11')
james.add_times(['0.9', '0.8'])
# get_coach_data 数据文件打开后返回的是一个 Athlete 类
# 所以 james 对象是一个 Athlete 的类对象,支持 Athlete 类对象的所有操作


print(james.name + "'s fastest times are：" + str(james.top3()))
print(julie.name + "'s fastest times are：" + str(julie.top3()))
print(mikey.name + "'s fastest times are：" + str(mikey.top3()))
print(sarah.name + "'s fastest times are：" + str(sarah.top3()))
