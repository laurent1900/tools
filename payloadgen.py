#coding:utf-8
import requests
from bs4 import BeautifulSoup

#生成数字对齐
def gen(num):
	f = open('num.txt','w+')
	n = str('%0'+str(num)+'d')
	for i in range(int('1'+'0'*num)):
		i = str(n % i)+'\n'
		f.write(i)
	f.close()

#生成数字不对齐
def gen2(num):
	f = open('num.txt','w+')
	# n = str('%0'+str(num)+'d')
	for i in range(1,int(num+1)):
		i = str(i)+'\n'
		f.write(i)
	f.close()

#查看出口IP
def iploc():
	url = 'http://ifconfig.me'
	r = requests.get(url)
	print(r.text)

if __name__ == '__main__':
	gen(3)
	# iploc()