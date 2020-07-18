import re


# pattern = re.compile("[0-9]{11}")
# print("请输入一个电话号码") 
# flag = 0
# str1 = input()
# if pattern.match(str1):
#     flag = 1
# while flag != 1:
#     print("输入有误 请重新输入：")
#     str1 =  input()  
#     if pattern.match(str1):
#         flag = 1
# result = str1[0:3] + "****" + str1[7:11]
# # result = pattern.sub("*",str1[])
# print("电话号码为：%s"%result)
str1 = "13855841334"
pattern = re.compile("^(1\d{2})(\d{4})(\d{4})$")
print(pattern.sub(r"\1****\3",str1))
# result = pattern.finditer(str1)
# for i in result:
#     print(i.group(1) + "****" + i.group(3))
# pattern = re.split("\w+")
#str1 = "as34dddd444zxc5435"
# result = re.split("\W+","as3,4d,ddd4,44zxc,5435")
# print(result)