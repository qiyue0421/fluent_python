# 一个浮点型数组的创建、存入文件和从文件读取的过程
from array import array
from random import random

# 使用生成器产生一个双精度浮点数组（类型码‘d’）
floats = array('d', (random() for i in range(10**7)))
print('查看数组最后一个元素：')
print(floats[-1])
fp = open('floats.bin', 'wb')
# 将数组存入二进制文件
floats.tofile(fp)
fp.close()

# 新建一个空的双精度浮点数组
floats2 = array('d')
fp = open('floats.bin', 'rb')
# 把1000万个浮点数从二进制文件里读取出来
floats2.fromfile(fp, 10**7)
fp.close()
print(floats2[-1])

