str=ord("你")#ord()里面只能有一个字符
print(str)#获取的字符的整数表示
str=chr(str)#整数表示转换成字符
print(str)
hai='ABc'.encode('ascii')
print(hai)# b'ABc'
hai='中国'.encode('UTF-8')#encode()的作用主要是str转码成bytes
print(hai)# b'\xe4\xb8\xad\xe5\x9b\xbd'
hai=b'\xe4\xb8\xad\xe5\x9b\xbd'.decode('UTF-8')#不需要单引号/双引号，decode()主要是将bytes转化成str
print(hai)
a=len(b'\xe4\xb8\xad\xe5\x9b\xbd')#len()对于bytes来说计算的是字节数
print(a)
a=len("中国")#len()对str来说计算的是字符串长度
print(a)