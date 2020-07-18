from bs4 import BeautifulSoup
import requests
import re

url = "http://www.runoob.com/python/python-100-examples.html"

html = requests.get(url).content.decode("utf-8")

soup = BeautifulSoup(html,"html.parser")

result = soup.find(id="content").ul.findAll("a")

lis = []
for i in result:
    #print(i.text)
    lis.append("http://www.runoob.com"+i.attrs["href"])
f = open("pythonTEXT.txt", "w",encoding="utf-8")
#print(lis)
n = 0
for i in lis:
    
    url2 = lis[n]

    html2 = requests.get(url2).content.decode("utf-8")

    soup2 = BeautifulSoup(html2,"html.parser")

    result2 = soup2.find(id="content").h1
    result3 = soup2.find(id="content").p.next_sibling.next_sibling
    result4 = soup2.find(id="content").p.next_sibling.next_sibling.next_sibling.next_sibling
    # print(result2.text+"\n")
    # print(result3.text+"\n")
    # print(result4.text+"\n")
    # print("\n" + "--------------------------------------")
    n += 1

    f.write( result2.text+"\n"+result3.text+"\n"+result4.text+"\n"+"--------------------------------------"+"\n" )

# 关闭打开的文件
f.close()
print("执行完毕")
# print(soup.div.span.attrs["class"])

# result = soup.div.contents[1].parents
# for i in result:
#     print(i)
# print(soup.div.contents[1].next_sibling.next_sibling)
# print(soup.findAll("a"))
# result = soup.findAll("a")
# for i in result:
#     print(i.text)
#     print(i.attrs["href"])

# print(result)
