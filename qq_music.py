import requests
import json
# 入口地址（暂时不考虑分页）
start_url='https://c.y.qq.com/splcloud/fcgi-bin/fcg_get_diss_by_tag.fcg?picmid=1&rnd=0.5763118180791627&g_tk=1806862358&jsonpCallback=a&loginUin=1009137312&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&categoryId=10000000&sortId=5&sin=0&ein=29'
# 伪装
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Referer':'https://y.qq.com/portal/playlist.html',
    'Host':'y.qq.com',
    #'Cookie':''
}
html=requests.get(start_url,headers=headers).text
json_dict=json.loads(html.strip('a()'))
# 遍历得到dissid
dissid_list=[]
for item in json_dict['data']['list']:
    dissid_list.append(item['dissid'])
print(dissid_list)
# 循环dissid_list 进行连接的拼接
# get_songmid_url_list=[]
# for dissid in dissid_list:
#     #返回songmid数据的链接
#     url="https://c.y.qq.com/qzone/fcg-bin/fcg_ucc_getcdinfo_byids_cp.fcg?type=1&json=1&utf8=1&onlysong=0&disstid={0}&format=jsonp&g_tk=1806862358&jsonpCallback=playlistinfoCallback&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0".format(dissid)
#     get_songmid_url_list.append(url)