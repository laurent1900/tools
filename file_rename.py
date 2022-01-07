#coding:utf-8
import os
import re

def file_rename():
    pwd = os.getcwd()
    for i in os.listdir(pwd):
        if 'xml' in i:
            a = re.sub(r"\(.*\)","",i)
            try:
                os.rename(i,a)
            except Exception as e:
                print('duplication file name: '+a)
                pass

if __name__ == '__main__':
    file_rename()