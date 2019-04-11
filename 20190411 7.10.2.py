import time
DEAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'


def clock(fmt=DEAULT_FMT):  # 参数化装饰器工厂函数
    def decorate(func):  # 真正的装饰器
        def clocked(*_args):  # 包装被装饰的函数
            t0 = time.time()
            _result = func(*_args)  # 被装饰函数的运行结果
            elapsed = time.time() - t0
            name = func.__name__
            args = '.'.join(repr(arg) for arg in _args)
            result = repr(_result)
            print(fmt.format(**locals()))
            return _result  # clocked会取代被装饰的函数，因此它应该返回被装饰的函数返回的值(没有返回值则为None)
        return clocked  # 返回clocked
    return decorate  # 返回decorate


if __name__ == '__main__':
    @clock()  # 关键在于此，装饰器工厂函数必须作为函数调用，返回真正的装饰器
    def snooze(seconds):
        time.sleep(seconds)
        return seconds

    for i in range(3):
        # snooze(.123)
        print(snooze(.123))
