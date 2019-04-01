import random
import bisect

SIZE = 7
# 随机数生成种子，如果不设置则每次随机生成的数不同
random.seed(1729)
my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE * 2)
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)
