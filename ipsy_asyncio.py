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
	iplist = ["1.202.88.88","1.202.88.91","1.92.79.57","106.37.108.78","106.38.112.222","111.203.143.6","111.203.143.7","111.203.163.113","111.203.163.116","111.203.163.119","113.105.157.200","113.105.157.203","114.113.237.201","114.113.237.214","114.116.233.245","114.116.248.139","114.116.249.168","114.116.255.157","117.78.24.36","117.78.24.37","119.3.186.22","119.3.215.30","119.3.216.56","120.46.216.17","121.12.168.82","121.36.34.56","121.36.38.90","121.36.46.78","121.36.59.222","123.60.210.190","124.70.12.186","124.70.125.129","124.70.125.166","124.70.126.102","124.70.29.247","124.70.3.132","124.70.64.205","125.88.255.56","139.9.116.175","183.60.229.74","183.60.229.78","183.60.229.83","183.60.229.86","183.60.229.87","183.60.255.101","183.60.255.108","183.60.255.97","203.93.19.57","203.93.19.62"]
	a = asyncio.run(run(iplist))
	for i in a:
		print(i[0]+'\t'+i[1])