#coding:utf-8
import nmap3
import json
import requests
import re
import time
import dingtalkchatbot.chatbot as cb
from multiprocessing import Pool,Queue


#端口扫描
def port_scan(host):
	nmap = nmap3.Nmap()
	result = nmap.scan_top_ports(host,args="--open -sV -n -T5 -Pn -p-")
	try:
		ports = result[host]['ports']
		name = []
		portid = []
		product = []
		service_name = []
		service = []
		if len(ports) != 0:
			for j in ports:
				portid.append(j['portid'])
				name.append(j['service']['name'])
				try:
					product.append(j['service']['product'])
				except Exception as e:
					product.append('unknown service')
			for i in zip(name,product):
				service_name.append(': '.join(i))
			for j in zip(portid,service_name):
				service.append(' '.join(j))
			return [host,service]
	except Exception as e:
		return [host,'0 port up']
		pass

#本地读取IP地址信息
def file_read(f):
	f = open(f,'r')
	text = []
	for i in f:
		text.append(i.strip())
	f.close()
	return text

#本地保存扫描结果
def mycallback(x):
	with open('nmap_result.txt','a+') as g:
		if x[1] != '0 port up':
			g.write('[+]'+str(x[0])+'\n>>>'+'\n>>>'.join(x[1])+'\n\n')
		else:
			pass
	g.close()

def dingding(msg):
	webhook = 'XXXXXX'
	secret = 'XXXXXX'
	ding = cb.DingtalkChatbot(webhook,secret=secret)
	ding.send_text(msg=msg, is_at_all=False)

#CMDB获取URL
def get_ips():
	url = "XXXXXX"
	headers = {
	"Host": "XXXX",
	"Cookie": "XXXXX"
	}
	r = requests.get(url,headers=headers,timeout=30)
	text = r.text
	text = text.split('\n')
	ips = []
	for i in text:
		try:
			ip = i.split(',')[7]
			if ip != '' and 'IP' not in ip:
				if '||' in ip:
					ip = ip.split('||')
					for i in ip:
						ips.append(i)
				else:
					ips.append(ip)
		except Exception as e:
			pass
	ips = set(ips)
	return list(ips)

def run(x):
	job_list = x
	p = Pool(10)
	for i in job_list:
		p.apply_async(port_scan,(i,),callback=result_get)
	p.close()
	p.join()

def result_get(x):
	result.append(x)

if __name__ == '__main__':
	result = []
	a = ''
	run(get_ips())
	for i in result:
		if i[1] != '0 port up':
			a += '[+]'+str(i[0])+'\n>>>'+'\n>>>'.join(i[1])+'\n\n'
	dingding(a)
