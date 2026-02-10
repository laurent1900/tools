#coding:utf-8
import dns.resolver
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
resolver = dns.resolver.Resolver()
resolver.nameservers = ['114.114.114.114']

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
	domains = ["pop.djbx.com","smtp.djbx.com","imap.djbx.com","mail.djbx.com","ptr1.dzbd.djbx.com","gxrc2103._domainkey.djbx.com","_dmarc.djbx.com","xiaoguan.djbx.com","softwarecenter.djbx.com","msoid.djbx.com","msg.djbx.com","msg.djbx.com","mail._domainkey.msg.djbx.com","_dmarc.msg.djbx.com","dzbd.djbx.com","dzbd.djbx.com","mail._domainkey.dzbd.djbx.com","_dmarc.dzbd.djbx.com","d2558e22ef7d5237.xiaoguan.djbx.com"]
	for i in domains:
		main(i)