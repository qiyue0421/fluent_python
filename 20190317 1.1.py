# 简单的有序纸牌类
from collections import namedtuple
import random

# 命名元组构建一个简单的类来表示一张纸牌
Card = namedtuple('Card', ['rank', 'suit'])


# 创建纸牌类
class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    # 将[]操作交给了self._cards列表，该方法使得对象可迭代
    def __getitem__(self, position):
        return self._cards[position]


# 实例化一叠纸牌
deck = FrenchDeck()

print(len(deck))

# 切片操作
print(deck[:20])

# 迭代对象
for card in deck:
    print(card)

# 反向迭代
for card_res in reversed(deck):
    print(card_res)

print(random.sample(list(deck), 5))
print(random.choice(deck))
