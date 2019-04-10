# 理解装饰器的一个关键特性：在被装饰的函数定义之后立即运行
# 保存被装饰的函数引用
registry = []


# 装饰器参数是一个函数，
def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    # 这里原封不动的返回 func：必须返回函数
    return func


@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


def f3():
    print('running f3()')


def main():
    print('running main()')
    print('register ->', registry)
    f1()
    f2()
    f3()


if __name__ == '__main__':
    main()


"""
输出结果：
running register(<function f1 at 0x0000015CCD107D08>)   # 很明显可以看出一旦模块运行，装饰器就被调用了
running register(<function f2 at 0x0000015CCD293A60>)   # 第二次运行
running main()
register -> [<function f1 at 0x0000015CCD107D08>, <function f2 at 0x0000015CCD293A60>]
running f1()      # 普通函数只有被明确调用后才执行
running f2()
running f3()
"""
