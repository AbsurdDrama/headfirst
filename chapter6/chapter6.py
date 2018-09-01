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
        return data.strip().split(',')
    except IOError as err:
        print('File Error' + str(err))
        return None


sarah = get_coach_data('sarah2.txt')
sarah_data = {'name': sarah.pop(0), 'bod': sarah.pop(0), 'times': sarah}

print(sarah_data['name'] + "'s fastest times are:"
      + str(sorted(set([sanitize(t) for t in sarah_data['times']]))[0:3]))
