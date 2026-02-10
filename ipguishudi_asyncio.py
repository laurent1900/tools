#coding:utf-8
import asyncio
import aiohttp
import io
import sys
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

headers = {
    "Host": "www.ip38.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Sec-Ch-Ua": '"Chromium";v="137", "Not/A)Brand";v="24"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Accept-Encoding": "gzip, deflate, br",
    "Priority": "u=0, i"
    }

async def main(ip):
    url = "https://www.ip38.com/ip/"+str(ip)+".htm"
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, headers=headers) as response:
            result = await response.text()
            result = BeautifulSoup(result,'html.parser').title.string
    return (ip,result)

async def run(iplist):
    tasks = [main(i) for i in iplist]
    results = await asyncio.gather(*tasks)
    return results

if __name__ == "__main__":
    iplist = ["106.8.136.104","110.218.176.11","110.218.176.13","112.224.160.60","117.132.188.205","117.136.16.144","14.17.3.224","162.216.149.253","172.235.40.131","198.235.24.124","201.7.170.246","202.93.141.18","212.102.40.218","218.26.159.226","223.104.143.18","223.104.150.110","223.104.161.198","223.104.195.44","223.104.211.28","80.82.77.33"]
    a = asyncio.run(run(iplist))
    for i in a:
        print(i)
        # print(i[0]+'\t\t'+i[1])
