print('hello world')
print(0b100)  # 二进制整数
print(0o100)  # 八进制整数
print(100)    # 十进制整数
print(0x100)  # 十六进制整数
print(123.456)    # 数学写法
print(1.23456e2)  # 科学计数法
"""
赋值运算符和复合赋值运算符

Version: 1.0
Author: 骆昊
"""
a = 10
b = 3
a += b        # 相当于：a = a + b
a *= a + 2    # 相当于：a = a * (a + 2)
print(a)      # 大家算一下这里会输出什么

"""
将华氏温度转换为摄氏温度

Version: 1.0
Author: 骆昊
"""
f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))
"""
输入半径计算圆的周长和面积

Version: 1.1
Author: 骆昊
"""
import math

radius = float(input('请输入圆的半径: '))
perimeter = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f'周长: {perimeter:.2f}')
print(f'面积: {area:.2f}')

"""
输入年份，闰年输出True，平年输出False

Version: 1.0
Author: 骆昊
"""
year = int(input('请输入年份: '))
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(f'{is_leap = }')