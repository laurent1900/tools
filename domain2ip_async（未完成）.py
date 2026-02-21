#coding:utf-8
import asyncio
from dns import resolver
 
async def main(domain):
	async with resolver.resolve(domain,'A') as res:
		answer = await res.response.answer
	return answer
	# try:
	# 	answer = await resolver.resolve(domain,'A')
	# 	return answer
	# except resolver.NoAnswer:
	# 	return 'No answer for '+domain
	# except resolver.NXDOMAIN:
	# 	return domain+' is not exist'
	# except Exception as e:
	# 	return e
		
 
async def run(domains):
	tasks = [main(domain) for domain in domains]
	results = await asyncio.gather(*tasks)
	return results
 
if __name__ == '__main__':
	domains = ['www.baidu.com', 'www.gamersky.com']
	results = asyncio.run(run(domains))
	print(results)
