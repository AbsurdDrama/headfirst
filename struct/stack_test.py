from struct.stack import Stack


def test_stack():
    s =  Stack()
    print(s.is_empty())
    s.push('a')
    print(s.all())
    s.push('中文')
    print(s.all())
    print(s.pop())
    print(s.is_empty())
    print(s.pop())
    print(s.is_empty())


test_stack()
