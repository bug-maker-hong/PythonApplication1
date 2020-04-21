hight=float(input("请输入你的身高："))
weight=float(input("请输入你的体重："))
BIM=weight/(hight**2)
print('Your BIM is %f'%(BIM))#直接--%--连接，不需要加逗号
if BIM<18.5:
    print("太轻了")
elif BIM<=25:
    print("正常")
elif BIM<=28:
    print("过重")
else :
    print("肥胖")
