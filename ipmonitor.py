#coding:utf-8
import nmap3
import json
from multiprocessing import Pool


#端口扫描
def port_scan(host):
	# ip_port_result = []
	nmap = nmap3.Nmap()
	result = nmap.scan_top_ports(host,args="--open -n")
	ports = result[host]['ports']
	ports_result = []
	if len(ports) != 0:
		for j in ports:
				ports_result.append(j['portid'])
		print(host,ports_result)
	else:
		print(host,'0 port up')
	# print(ip_port_result)

#主机发现，扫描全部外网IP，检查启用状态
def host_discovery(ip):

	# host_up = []
	# host_down = []

	nmap = nmap3.NmapHostDiscovery()
	result = nmap.nmap_no_portscan(ip)
	host_status = result['runtime']['summary']
	if '(1 host up)' in host_status:
		port_scan(ip)
		# host_up.append(ip)
	elif '(0 hosts up)' in host_status:
		# host_down.append(ip)
		print(ip+" INACTIVE")

	# return host_up,host_down

#读取IP地址信息
def file_read(f):
	f = open(f,'r')
	text = f.readline()
	f.close()
	ips = json.loads(text)
	ips = ips.keys()
	return list(ips)

def run():
	job_list = file_read('ip.json')
	p = Pool(5)
	for i in job_list:
		p.apply_async(host_discovery,(i,))
	p.close()
	p.join()

if __name__ == '__main__':
	# results = []
	# job_list = file_read('ip2.json')
	# p = Pool(5)
	# for i in job_list:
	# 	p.apply_async(host_discovery,(i,))
	# p.close()
	# p.join()
	run()
