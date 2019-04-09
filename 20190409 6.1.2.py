# 使用函数实现“策略”模式
from collections import namedtuple

# 客户类，命名元组接受两个参数：类名、字段名
Customer = namedtuple('Customer', 'name fidelity')


# 商品类
class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.quantity * self.price


# 上下文
# 购物类
class Order:
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        # 订单列表
        self.cart = list(cart)
        self.promotion = promotion

    # 订单总价
    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    # 订单减去折扣
    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total:{:2f} due: {:2f}>'
        return fmt.format(self.total(), self.due())


# 第一个具体策略
# 客户积分大于1000分可以享受折扣
def FidelityPromo(order):
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


# 第二个具体策略
# 订单中单个商品的个数大于20可以享受折扣
def BulkItemPromo(order):
    discount = 0
    # 遍历订单列表中的每个商品
    for item in order.cart:
        # 检索数量大于20的商品
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount


# 第三个具体策略
# 订单中不同商品达到10个或以上，享受折扣
def LargeOrderPromo(order):
    # 利用集合推导式获取订单中不同商品的列表
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07


promos = [FidelityPromo, BulkItemPromo, LargeOrderPromo]


# 选择最佳策略
def best_promo(order):
    return max(promo(order) for promo in promos)


# 实例化客户joe，积分为0
joe = Customer('John Doe', 0)
# 实例化客户ann，积分为1000
ann = Customer('Ann Smith', 1000)

# 创建订单列表，通过实例化商品类构建
cart = [LineItem('banana', 4, .5), LineItem('apple', 10, 1.5), LineItem('watermelon', 5, 5.0)]
# 构建单个商品数量大于20的订单
banana_cart = [LineItem('banana', 30, .5), LineItem('apple', 10, 1.5)]
# 构建包含10个不同商品的订单
larger_cart = [LineItem(str(item), 1, 1.0) for item in range(10)]

# 实例化一次消费，客户joe，折扣策略为根据积分计算
print(Order(joe, cart, FidelityPromo))
"""
结果为
<Order total:42.000000 due: 42.000000>
因为该客户的积分为0，不享受折扣
"""

# 实例化一次消费，客户ann，折扣策略为第一个策略
print(Order(ann, cart, FidelityPromo))
"""
结果为
<Order total:42.000000 due: 39.900000>
因为该客户的积分为1000
"""

# 来看看第二个策略是否可行
print(Order(joe, banana_cart, BulkItemPromo))
"""
结果为
<Order total:30.000000 due: 28.500000>
该订单中香蕉的数量已经超过了20
"""

# 来看看第三个策略是否可行
print(Order(joe, larger_cart, LargeOrderPromo))
"""
结果为
<Order total:10.000000 due: 9.300000>
该订单中有10种不同的商品
"""
