#coding:utf-8
import asyncio
import aiohttp
import io
import sys
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

headers = {
	"Host": "ip38.com",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"Cookie": "Hm_lvt_2343fe6f116e92cb302292841b8592e1=1641955179; Hm_lpvt_2343fe6f116e92cb302292841b8592e1=1641955463"
	}

async def main(ip):
	url = "https://ip38.com/ip.php?ip="+str(ip)
	async with aiohttp.ClientSession() as session:
		async with session.get(url=url, headers=headers) as response:
			result = await response.text()
			result = BeautifulSoup(result,'html.parser').font.text.split('\xa0\xa0')[1]
	return (ip,result)

async def run(iplist):
	tasks = [main(i) for i in iplist]
	results = await asyncio.gather(*tasks)
	return results

if __name__ == "__main__":
	iplist = ["10.223.10.12","10.223.10.13","10.223.100.25","10.223.105.10","10.223.105.11","10.223.105.22","10.223.110.7","10.223.138.19","10.223.138.20","10.223.138.23","10.223.138.24","10.223.138.30","10.223.138.31","10.223.138.32","10.223.138.45","10.223.138.46","10.223.138.69","10.223.138.81","10.223.143.16","10.223.143.20","10.223.143.21","10.223.143.23","10.223.143.38","10.223.143.44","10.223.143.7","10.223.143.8","10.223.15.26","10.223.153.6","10.223.25.5","10.223.25.6","10.5.78.121","106.112.144.253","106.112.147.77","106.118.184.127","106.8.145.1","111.31.188.66","111.31.188.77","113.246.197.81","116.131.194.150","116.148.99.10","117.11.45.115","117.11.45.139","119.39.18.166","120.228.6.171","120.228.6.178","120.228.6.179","120.228.7.157","120.228.7.171","120.228.7.42","175.0.224.118","175.0.225.237","175.0.227.255","175.8.127.206","175.9.225.110","175.9.231.185","175.9.231.32","183.197.187.163","183.197.187.249","183.197.188.87","183.198.113.122","183.199.58.217","218.69.242.29","221.197.28.93","221.221.153.22","36.106.183.151","36.106.79.201","36.143.74.119","36.21.68.247","47.121.184.228","58.20.24.151","58.20.74.132","58.20.74.59","60.26.94.54"]
	a = asyncio.run(run(iplist))
	for i in a:
		print(i[0]+'\t\t'+i[1])