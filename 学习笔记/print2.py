
#瞎写的code
str='hello,%s'%'world'
print(str)
str='hi,%s,you have $%9d.'%('Michael',1000000)
print(str)#自己体会"一一对应"
str='%.4f'%3.1415926#数字的表述和C语言差不多
print(str)
str='growth rate:%d %%' % 7
print(str)#%%表示%“转义”
r1=72
r2=85
r=((r2-r1)/r1)*1e2
print('%.1f %%'% r)#little test
