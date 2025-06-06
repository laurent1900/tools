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
	iplist = []
	a = asyncio.run(run(iplist))
	for i in a:
		print(i[0]+'\t\t'+i[1])