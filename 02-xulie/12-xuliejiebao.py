# -- coding: utf-8 --
'''
    序列解包
        用于元组，列表，字典。可以让我们方便的对多个变量赋值
            x, y, z = 10, 20, 30
            x, y, z = (10, 20, 30)

        字典
            1> 对键进行解包
            2> 对键值对进行解包
            3> 对值进行解包

'''
a = {'name': 'pao', 'age': 13}
# c, d, e = a 会报错
# c = a # 就成赋值操作了
c, d = a # 默认的是对字典的 键进行解包
print(c)

e, f = a.items() #对键和值进行解包
print(e)

g, h = a.values() # 对值进行解包
print(g)