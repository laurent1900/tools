#coding:utf-8
import dns.resolver

def main(i):
	try:
		domain = i
		result = dns.resolver.resolve(domain, 'A')
		for i in result.response.answer:
			for j in i.items:
				if j.rdtype == 1:
					print(domain,j.address)
	except Exception as e:
		print(e)
		pass

if __name__ == '__main__':
	domains = ["www.baidu.com"]
	for i in domains:
		main(i)