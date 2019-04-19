from array import array
import math


class Vector2d:
    # 类属性
    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)  # 转换为浮点型
        self.__y = float(y)

    @property   # 将读值方法标记为特性
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

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

    # 转换为字节
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    # 取模运算
    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    # 使实例变成可散列的需要实现hash
    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    # 计算角度
    def angle(self):
        return math.atan2(self.y, self.x)

    # 格式化输出
    def __format__(self, format_spec=''):
        if format_spec.endswith('p'):        # 极坐标表示
            format_spec = format_spec[:-1]  # 删除'p'后缀
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:       # 直角坐标表示
            coords = self
            outer_fmt = '({}. {})'
        # 将format_spec应用到向量的各个分量上，构建一个可迭代的格式化字符
        components = (format(c, format_spec) for c in coords)
        return outer_fmt.format(*components)  # 将格式化字符串带入要输出的格式中


v1 = Vector2d(3, 4)
print(v1.x, v1.y)

x, y = v1
print(x, y)

print(v1)
