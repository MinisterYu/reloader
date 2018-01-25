#coding:utf-8
'''
Created on 2018年1月23日

@author: ministeryu
'''
from main.reloader import run_with_reloader
extra_files = ['./words','./info']

def reload_test(s):
    print open('./info').read() 
    
if __name__ == '__main__':
    run_with_reloader(reload_test, extra_files ,'hello world')
    
    
