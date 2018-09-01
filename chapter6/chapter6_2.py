"""优化函数构建"""


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


def get_coach_data(filename):
    try:
        with open(file=filename) as f:
            data = f.readline()
            tmp = data.strip().split(',')
            return ({
                'Name': tmp.pop(0),
                'DOB': tmp.pop(0),
                'Times': str(sorted(set([sanitize(t) for t in tmp]))[0:3])
            })
    except IOError as err:
        print('File Error' + str(err))
        return None


sarah = get_coach_data('sarah2.txt')
print(sarah['Name'] + "'s fastest times are:"
      + sarah['Times'])
