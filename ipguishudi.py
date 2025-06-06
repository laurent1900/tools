#coding:utf-8
import requests
import io
import sys
import threadpool
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

def main(ip):
	url = "https://ip38.com/ip.php?ip="+str(ip)
	headers = {
				"Host": "ip38.com",
				"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
				"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				"Cookie": "Hm_lvt_2343fe6f116e92cb302292841b8592e1=1641955179; Hm_lpvt_2343fe6f116e92cb302292841b8592e1=1641955463"
	}
	try:
		result = requests.get(url,headers=headers,timeout=30)
		soup = BeautifulSoup(result.text,'html.parser')
		html = soup.font.text
		ip_loc.append((ip,html))
	except Exception as e:
		print(ip+' fail','失败原因：'+str(e))
		pass


if __name__ == "__main__":
	ip_loc = []
	pool = threadpool.ThreadPool(5)
	ip_list = []
	req = threadpool.makeRequests(main,ip_list)
	for i in req:
		pool.putRequest(i)
	pool.wait()

	for i in ip_loc:
		print(i[0]+'\t'+i[1].split()[1])