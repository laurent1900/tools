#coding:utf-8
import dns.resolver
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
resolver = dns.resolver.Resolver()
resolver.nameservers = ['8.8.8.8']

def main(i):
    try:
        domain = i
        result = resolver.resolve(domain, 'A')
        for i in result.response.answer:
            for j in i.items:
                if j.rdtype == 1:
                    print(domain,j.address)
    except Exception as e:
        print(i,e)
        pass

if __name__ == '__main__':
	domains = ["www.baidu.com"]
	for i in domains:
		main(i)
