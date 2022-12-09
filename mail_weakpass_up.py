#condig:utf-8
import smtplib

def getInfo():
	host = 'mail.xxx.com'
	port = 25
	f = open('xxx.txt','r')
	for i in f:
		username = i.split(',')[0].strip()
		password = i.split(',')[1].strip()
		suffix = '@xxx.com'
		account = username+suffix
		smtp = smtplib.SMTP(host,port)
		try:
			smtp.login(account,password)
			print(account,password)
			smtp.quit()
		except Exception as e:
			# print(e)
			pass
	f.close()

if __name__ == '__main__':
	getInfo()