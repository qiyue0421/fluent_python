"""
name:标签名字
content:内容
cls:class属性
attrs:关键字参数
"""


# HTML标签生成函数
def tag(name, *content, cls=None, **attrs):
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value) for attr, value in attrs.items())
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)


print(tag('br'))
print(tag('p', 'hello'))
print(tag('p', 'hello', 'world'))

# cls只能作为关键字参数传入
print(tag('p', 'hello', 'world', cls='sidebar'))

# 具名参数name会被准确捕获
print(tag(content='testing', name='img'))
# <img content="testing" />

# 同名键会被绑定到具名参数上
my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'Sunset.jpg', 'cls': 'framed'}
print(tag(**my_tag))
# <img title="Sunset Boulevard" src="Sunset.jpg" class="framed" />
