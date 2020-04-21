print('\\\n\\')#和C语言差不多"\\"表示的是"\"的意思
print(r'\\\n\\')#用r''表示''内的字符串默认不转义,只能用单引号
print(r'''我
爱
学习''')#'''......'''表示多行输出ps:可以在在前面加r使用
print(3<2)#输出为False
print(3<2 and 2>1 or not(1<3))#python里的and or not相当于C语言里的“&&”，“||”，“！”
print('\u4e2d')
str=ord("你")#ord()里面只能有一个字符
print(str)#获取的字符的整数表示
str=chr(str)#整数表示转换成字符
print(str)
