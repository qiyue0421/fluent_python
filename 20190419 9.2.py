from array import array
import math


class Vector2d:
    # 类属性
    typecode = 'd'

    def __init__(self, x, y):
        self.x = float(x)  # 转换为浮点型
        self.y = float(y)

    # 将实例变成可迭代对象，实现拆包功能
    def __iter__(self):
        return (i for i in (self.x, self.y))

    # repr方法使用{!r}获取各个分量的表现形式，然后插值
    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    # print函数会调用str函数
    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    # 取模运算
    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))


v1 = Vector2d(3, 4)
print(v1.x, v1.y)

x, y = v1
print(x, y)

v1
print(v1)

