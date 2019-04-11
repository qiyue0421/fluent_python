# 使用 functools.lru_cache 做备忘，这个装饰器实现了备忘功能，避免了传入相同的参数时重复计算
# 我们可以用两种不同的方式实现斐波那契数列做对比，
import time
import functools


# 第一个方法：递归方式
def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ','.join(repr(arg) for arg in args)
        print('[%0.7fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked


@clock
def fibonaci_1(n):
    return n if n < 2 else fibonaci_1(n-2) + fibonaci_1(n-1)


# 第二种方式：使用递归+缓存，速度更快
@functools.lru_cache()
@clock
def fibonaci_2(n):
    return n if n < 2 else fibonaci_2(n-2) + fibonaci_2(n-1)


if __name__ == '__main__':
    print('第一种方式：')
    fibonaci_1(6)
    print()
    print('第二种方式：')
    fibonaci_2(6)
# 查看输出，对比两种方式，可以看出第一种方式 factorial(1)调用了8次，factorial(2)调用了5次
# 而第二种方式每个值只会被调用一次
# 如果是计算 factorial(30)我们可以想得到第一种方式将会无比繁杂
