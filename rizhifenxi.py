#coding:utf-8
import pandas as pd
import numpy as np
import io
import sys
import threadpool
import requests
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('max_colwidth',200)

def main(ip):
	url = "https://ip38.com/ip.php?ip="+str(ip)
	# print(url)
	headers = {
				"Host": "ip38.com",
				"Connection": "close",
				"Cache-Control": "max-age=0",
				"sec-ch-ua-mobile": "?0",
				"sec-ch-ua-platform": "Windows",
				"DNT": "1",
				"Upgrade-Insecure-Requests": "1",
				"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
				"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				"Sec-Fetch-Site": "none",
				"Sec-Fetch-Mode": "navigate",
				"Sec-Fetch-User": "?1",
				"Sec-Fetch-Dest": "document",
				"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
				"Cookie": "Hm_lvt_2343fe6f116e92cb302292841b8592e1=1641955179; Hm_lpvt_2343fe6f116e92cb302292841b8592e1=1641955463"
	}
	result = requests.get(url,headers=headers,timeout=30)
	soup = BeautifulSoup(result.text,'html.parser')
	html = soup.font.text.replace(u'\xa0\xa0', ' ')
	ip_loc.append((ip,html))
	# print(soup.font.text.replace(u'\xa0\xa0', ' '))

if __name__ == '__main__':
	data = pd.read_table('2022.01.16.all.log',header=None,sep=' ') #读取Excel

	top10_200 = data.loc[data[6].isin([200])].loc[:,0].value_counts().head(10)
	print('200:')
	print(top10_200,'\n')

	top10_302 = data.loc[data[6].isin([302])].loc[:,0].value_counts().head(10)
	print('302:')
	print(top10_302,'\n')

	top10_400 = data.loc[data[6].isin([400])].loc[:,0].value_counts().head(10)
	print('400:')
	print(top10_400,'\n')

	top10_403 = data.loc[data[6].isin([403])].loc[:,0].value_counts().head(10)
	print('403:')
	print(top10_403,'\n')



	ips = [] #初始化问题IP列表

	ip_loc = [] #初始化问题IP归属地列表

	list_a = data.loc[(data[6].isin([302])) & (data[5].str.contains('fileid='))].loc[:,0].value_counts().index #恶意文件下载问题IP

	list_b = data.loc[(data[6].isin([302])) & (data[5].str.contains('fileid='))].loc[:,0].value_counts().values #访问次数

	dict_c = dict(zip(list_a,list_b)) #将问题IP和访问次数合并成字典

	#添加问题IP至ips列表
	for i in list_a:
		ips.append(i)

	#查询IP归属地
	pool = threadpool.ThreadPool(10) #初始化10个线程
	url_list = ips #添加目标
	req = threadpool.makeRequests(main,url_list) #发起查询请求
	for i in req:
		pool.putRequest(i)
	pool.wait()

	for i in ip_loc:
		key = i[0]
		value1 = i[1].split()[1] #IP归属地
		value2 = str(dict_c[key])+'次' #访问次数
		value3 = [value1,value2] #将IP归属地和访问次数拼接成一个列表
		dict_c[key] = value3 #将新值赋值给字典dict_c

	print("以下IP访问了文件下载URL并触发了跳转，疑似恶意访问：")
	for i in dict_c:
		print(i,dict_c[i][0],dict_c[i][1])