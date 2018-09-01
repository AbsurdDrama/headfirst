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


james = get_coach_data('james.txt')
julie = get_coach_data('julie.txt')
mikey = get_coach_data('mikey.txt')
sarah = get_coach_data('sarah.txt')

clean_james = []
for each in james:
    clean_james.append(sanitize(each))

print(sorted(james))
print(sorted(clean_james))

# TODO: 列表推导式

print(sorted([sanitize(each) for each in julie])[0:3])
print(sorted([sanitize(each) for each in mikey]))
print(sorted([sanitize(each) for each in sarah]))
