# 一个简单的二维向量类
from math import hypot


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 将实例对象用字符串表达出来
    def __repr__(self):
        return 'Vector({!r}, {!r})'.format(self.x, self.y)

    # hypot()函数返回欧几里德范数 sqrt(x*x + y*y)
    def __abs__(self):
        return hypot(self.x, self.y)

    # 模值变布尔值，如果向量模是0，则返回False
    def __bool__(self):
        return bool(abs(self))
        # 可以使用or运算符：若x的值等价为真，返回x值；否则返回y的值
        # return bool(self.x or self.y)

    # +运算，返回值是新创建的向量对象，被操作的两个向量不改变
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # *运算
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


v1 = Vector(2, 3)
print(v1)
v2 = Vector(4, 5)
print(v2)
print(bool(v2))
print(abs(v1 + v2))
