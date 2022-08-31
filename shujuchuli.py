#coding:utf-8
import pandas as pd
import numpy as np
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('max_colwidth',200)

def main():
	pass

if __name__ == '__main__':
	# main()
	#文件读取
	data = pd.read_table('2022.01.15.all.log',header=None,sep=' ') #读取Excel
	# data = pd.read_json('网络攻击-从2021-12-13至2022-01-11.json')
	# print(data.isna().sum().sum())
	# print(data.isnull().sum())
	# print(data[data.isnull().T.any() == True])

	#数据信息预览
	# print(data.shape) #查看数据维度，行数、列数
	# print(data.sample()) #数据抽样
	# print(data.head(3)) #查看数据前3行
	# print(data.info()) #查看数据基本信息
	# print(data)
	# print(data.loc[:,[0]].value_counts())
	print(data.loc[(data[6].isin([302])) & (data[5].str.contains('fileid='))].loc[:,0].value_counts())

	# print(data.loc[:,['sip','dip','rule_name']].describe()) #通过loc定位想看的行和列并展示统计值，方便分析
	# print(data.loc[:,['sip','dip','rule_name']])
	# df = data.loc[:,['sip','dip','rule_name']]
	# print(df.groupby(['sip','dip','rule_name']).agg('size').sort_values(0,ascending=False))
