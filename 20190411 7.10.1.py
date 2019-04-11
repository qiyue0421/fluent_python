# 参数化装饰器
# python把被装饰的函数作为第一个参数传给装饰器，那么如何传入其他参数给装饰器呢
# 解决办法是：创建一个装饰器工厂函数，把参数传给它，返回一个装饰器，然后再把它应用到要装饰的函数上


registry = set()


def register(active=True):  # 接受一个可选的关键字参数
    def decorate(func):  # 这个内部函数才是真的装饰器，注意它的参数是一个函数
        print('running register(active=%s) -> decorate(%s)' % (active, func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)
        return func  # decorate 是装饰器，所以需要返回一个函数
    return decorate  # register 是装饰器工厂函数，因此返回 decorate


@register(active=False)  # 装饰器工厂函数必须作为函数调用，并且传入所需参数
def f1():
    print('running f1()')


@register()  # 即使不传入参数，register也必须作为函数被调用，用来返回真正的装饰器 decorate
def f2():
    print('running f2()')
