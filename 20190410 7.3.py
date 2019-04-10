# 使用装饰器改进“策略”模式
"""
优点：
1、促销策略函数无需使用特殊名称（即不用以_promo结尾）
2、@promotion装饰器突出了被装饰的函数的作用，还便于临时禁用某个促销策略：只需要把装饰器注释掉
3、促销折扣策略可以在其他模块中定义，在系统中的任何地方都行，只要使用@promotion装饰即可
"""

promos = []


# promotion装饰器把promo_func添加到列表中，并原封不动的返回
def promotion(promo_func):
    # 所有被装饰的函数都会自动添加到promos列表中，防止忘记添加的情况发生
    promos.append(promo_func)
    return promo_func


@promotion
def Fidelity(order):
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


@promotion
def BulkItem(order):
    discount = 0
    # 遍历订单列表中的每个商品
    for item in order.cart:
        # 检索数量大于20的商品
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount


@promotion
def LargeOrder(order):
    # 利用集合推导式获取订单中不同商品的列表
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07


# 选择最佳策略，只需要调用列表中存在的策略即可（依赖于promos列表）
def best_promo(order):
    return max(promo(order) for promo in promos)
