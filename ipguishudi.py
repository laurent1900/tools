#coding:utf-8
import requests
import io
import sys
import threadpool
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

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
	print(soup.font.text.replace(u'\xa0', ' '))


if __name__ == "__main__":
	pool = threadpool.ThreadPool(10)
	url_list = ["114.114.114.114"]
	req = threadpool.makeRequests(main,url_list)
	for i in req:
		pool.putRequest(i)
	pool.wait()