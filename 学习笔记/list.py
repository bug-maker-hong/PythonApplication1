

#瞎写的code
classmate=['Tom','Bob','Tracy',123,2>3]#list列表--列表里的元素可以不是同一个数据类型--,可直接对列表里的元素重新赋值
print(classmate)
print(len(classmate))#len()求出列表里元素的个数
print(classmate[1])#访问list列表的索引是从“0”开始的，这点和C语言的数组是一样的
print(classmate[-1])#索引带负号，说明是从后往前的第几个元素
classmate.append('Adam')
print(classmate)#利用append()函数在列表的--末尾--添加元素
classmate.insert(1,'Jake')
print(classmate)#利用insert()函数在列表的某个特殊位置插入新的元素
classmate.pop(0)
print(classmate)#利用pop()函数默认删除列表的最后一个元素，也可指定--在pop()里添加索引号即可--
classes=['teacher',classmate]
print(classes)#一个列表也可以是另一个列表里的元素--在另一个列表里的长度为1--，
#在这里可以把classes看成二维数组，访问classmate里的元素可用classmate[],也可用class[1][?]--"1"是列表在classes里的索引号
print(len(classes))
#tuple(元组)可以理解为不可改变长度的list---指向永远不变---
