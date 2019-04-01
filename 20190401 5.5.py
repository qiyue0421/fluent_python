import random


# 该类的实例使用任意可迭代对象构建，调用实例时会取出一个元素
class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    # bingo实例可以作为函数调用，bingo.pick()的快捷方式是bingo()
    def __call__(self):
        return self.pick()

    # 用字符串形式显示对象
    def __repr__(self):
        return '{!r}'.format(self._items)


bingo = BingoCage(range(3))
print(bingo)
print(bingo.pick())
print(bingo())
