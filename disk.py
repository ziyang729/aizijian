#!/usr/bin/env python
'''
这是一个帮助手册
您可以使用这个模块来进行对服务器磁盘进行一个基本查询
{ '/' | '/boot' | 'dev' }分区的python模块
选项有{ 'used" | 'free' | 'total' }
'''
import sys
import psutil
disk_info=sys.argv[1]
disk_option=sys.argv[2]
def memory(disk_info,disk_option):
'''
这是一个查看{ '/' | '/boot' | 'dev' }分区的python模块
其中,可以查看的选项有{ 'used" | 'free' | 'total' }
'''
	if disk_info=='/':
		disk_info=psutil.disk_usage(disk_info)
		disk_value=getattr(disk_info, disk_option)
		num=disk_value/1024/1024/1024
		rounded_num=round(num,2)
		print(rounded_num,'G')
	elif disk_info=='/dev':
		disk_info=psutil.disk_usage(disk_info)
		disk_value=getattr(disk_info, disk_option)
		num=disk_value/1024/1024/1024
		rounded_num=round(num,2)
		print(rounded_num,'G')
	elif disk_info=='/boot':
		disk_info=psutil.disk_usage(disk_info)
		disk_value=getattr(disk_info, disk_option)
		num=disk_value/1024/1024/1024
		rounded_num=round(num,2)
		print(rounded_num,'G')
if __name__=="__main__":
        memory(disk_info,disk_option)
