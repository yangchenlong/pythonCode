# 第三章
# 3.1 列表是什么
colors = ['red', 'blue', 'yellow', 'pink']
print(colors)

# 3.1.1访问列表元素
print(colors[0])

# 3.1.2索引从0而不是1开始
print(colors[0])  # red
print(colors[3])  # pink
print(colors[-1])  # pink ，-1从后面开始取

# 3.1.3使用列表中的各个值
bicyles = ['trek', 'cannondale', 'redline']
message = "My first bicyles was a " + bicyles[0].title() + "."
print(message)

# 3.2.1修改列表元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# 3.2.2在列表中添加元素
motorcycles.append('ducati')  # 在末尾添加元素
print(motorcycles)
motorcycles.insert(0, 'honda')  # 在指定位置插入元素
print(motorcycles)

# 3.2.3从列表中删除元素-使用del语句删除元素
del motorcycles[0]  # 删除第1个元素
print(motorcycles)
# 3.2.3从列表中删除元素-使用pop()方法删除元素
poped_motorcycle = motorcycles.pop()  # 默认是删除最后一位并返回该删除的值。也可以指定某个删除的元素，譬如：pop(2)
print(poped_motorcycle)
print(motorcycles)

# 3.2.3从列表中删除元素-根据值删除元素
print(motorcycles)  # ['ducati', 'yamaha', 'suzuki']
print(motorcycles.remove('suzuki'))  # 返回None
print(motorcycles)

# 3.3组织元素
# 3.3.1方法sort()对列表进行永久性排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)  # 添加这个参数reverse=True可以按字母顺序相反来排列
# print(cars)

# 3.3.2 函数sorted()对列表进行临时排序
print("原始列表： ")
print(cars)
print("临时列表： ")
print(sorted(cars))
print(cars)

# 3.3.3方法reverse()倒着打印列表
print(cars)
print(cars.reverse())  # None
print(cars)

# 3.3.4 函数len()确定列表的长度
print(len(cars))
