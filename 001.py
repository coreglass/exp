x = int(input("第一个数字是："))
y = int(input("第二个数字是："))
z = int(input("第三个数字是："))

if x > y :
    if x > z:
        print("最大的数是：%d"%x)
    else:
        print("最大的数是：%d"%z)
elif x > z:
    if y > z:
        print("最大的数是：%d"%y)
    else:
        print("最大的数是：%d"%z)
       

            
