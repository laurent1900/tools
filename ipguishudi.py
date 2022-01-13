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
	url_list = ["112.49.203.202","111.203.85.226","124.78.48.171","40.77.167.45","40.77.167.7","112.49.210.253","157.55.39.171","157.55.39.202","157.55.39.158","124.65.230.182","207.46.13.103","157.55.39.29","219.239.42.59","1.202.31.94","40.77.167.17","220.196.194.23","116.132.223.158","101.84.62.19","223.71.52.133","39.175.221.149","13.66.139.0","121.227.127.93","39.175.221.49","23.100.232.233","40.94.94.91","52.168.53.30","40.94.94.85","111.201.237.46","42.236.10.114","40.77.167.39","210.22.245.226","210.22.245.219","119.84.234.157","111.201.233.151","101.89.239.120","87.101.94.69","70.113.252.152","61.151.207.205","61.151.207.112","61.151.178.249","61.151.178.163","58.219.163.211","58.213.83.226","40.77.191.249","40.77.188.161","39.172.157.248","36.110.199.35","27.115.124.70","223.88.46.77","223.166.151.191","220.196.193.4","197.184.179.184","197.184.176.61","197.153.72.233","159.89.181.182","104.47.6.254","101.89.239.238"]
	req = threadpool.makeRequests(main,url_list)
	for i in req:
		pool.putRequest(i)
	pool.wait()