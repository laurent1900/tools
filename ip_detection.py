#coding:utf-8
import nmap3
import re
from IPy import IP
from IPy import IPSet

def C_detection(args):
	# print(args)
	ip1 = args[0]
	ip2 = args[1]
	# print(type(ip1),type(ip2))
	if ip_detection(ip1) == 'up' or ip_detection(ip2) == 'up':
		print(ip1+' existence')
	else:
		print(ip1+' non-existent')

def ip_detection(ip):
	nmap = nmap3.NmapHostDiscovery()
	try:
		result = nmap.nmap_no_portscan(ip)
		if ip in result:
			return result[ip]['state']['state']
		else:
			return 'down'
	except Exception as e:
		print(e)
		return None

def ip_processing(ip):
	ip = IP(str(ip.strip()))
	ip_start = str(ip[1])
	ip_end = str(ip[-2])
	return ip_start,ip_end


if __name__ == '__main__':
	# ip = "10.0.45.0/24"
	# C_detection(ip_processing(ip))
	# s = IPSet([IP('10.0.0.0/8')])
	# print(s)
	ip = IP("10.0.0.0/16")
	first_ips = []
	end_ips = []
	for i in ip:
		first_ip = re.match(r"(\d{1,3}\.){3}1$",str(i))
		end_ip = re.match(r"(\d{1,3}\.){3}254$",str(i))
		if first_ip != None:
			# print(first_ip,end_ip)
			first_ips.append(str(i))
		elif end_ip != None:
			end_ips.append(str(i))
	for i in zip(first_ips,end_ips):
		# print(type(i))
		C_detection(i)