# 在查询时把非字符串的键转换成字符串


# 继承自dict类
class StrKeyDict0(dict):
    # 找不到键使用这个方法
    def __missing__(self, key):
        # 如果找不到的键是字符串，则抛出异常,如果没有该判断，则代码陷入无限递归
        if isinstance(key, str):
            raise KeyError(key)
        # 如果找不到的键不是字符串（可能是数值），则返回字符串形式的键再次查找
        return self[str(key)]

    def get(self, key, default=None):
        try:
            # get方法把查找工作用self[key]的形式委托给__getitem__，这样在查找失败之前还可以通过__miss__再给某个键一个机会
            return self[key]
        # 找不到key，则返回默认值
        except KeyError:
            return default

    # 包含操作
    def __contains__(self, key):
        # 注意，这里查找了两次，先用键本身查找，再用字符串形式的值查找
        return key in self.keys() or str(key) in self.keys()


d = StrKeyDict0([('2', 'two'), ('4', 'four')])
print('如果键本来就是字符串形式')
print(d['2'])
print('\n如果键不是字符串形式')
print(d[4])
print('\n如果没有找到键')
# print(d[1])

print('\nGET方法')
print(d.get('2'))
print(d.get(4))
print(d.get(1, 'N/A'))

print('\n包含操作')
print(2 in d)
print(1 in d)
