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
	try:
		result = requests.get(url,headers=headers,timeout=30)
		soup = BeautifulSoup(result.text,'html.parser')
		html = soup.font.text.replace(u'\xa0\xa0', ' ').replace('IP详细地址：','')
		ip_loc.append((ip,html))
	except Exception as e:
		print(ip+' fail','失败原因：'+str(e))
		pass


if __name__ == "__main__":
	ip_loc = []
	pool = threadpool.ThreadPool(5)
	url_list = ["116.196.90.163","111.203.85.162","111.203.85.162","111.203.85.162","111.203.85.162","111.203.85.162","111.203.85.162","111.203.85.162","111.203.85.140","219.239.42.88","111.203.85.162","111.203.85.162","39.105.180.130","111.203.85.162","111.203.85.162","111.203.85.162","111.203.85.163","123.56.111.7","111.203.85.162","111.203.85.162","111.203.85.161","111.203.85.162","47.95.246.200","47.95.246.200","60.190.243.164","47.95.246.200","47.95.246.200","111.203.85.162","111.203.85.162","111.203.85.161","111.203.85.162","47.95.246.200","47.95.246.200","60.190.243.164","47.95.246.200","47.95.246.200","111.203.85.162","39.105.180.130","39.105.167.59","111.203.85.162","39.96.126.202","123.57.72.209","47.95.234.135","39.96.126.202","39.107.240.39","39.107.240.39","111.203.85.161","111.203.85.162","39.105.79.92","39.105.79.92","111.203.85.162"]
	req = threadpool.makeRequests(main,url_list)
	for i in req:
		pool.putRequest(i)
	pool.wait()

	for i in ip_loc:
		print(i[0],i[1].split()[1])