import random
from urllib import request

import requests

fpr=open('host.txt','r')
fpw = open('proxies.txt','w')

ips=fpr.readlines()
proxys=list()
for p in ips:
    ip=p.strip('\n').split('\t')
    pro=dict()
    pro['https'] = ip[0] + ':' + ip[1]
    print(pro)
    try:
        response = requests.get('https://www.baidu.com', proxies=pro,timeout=2)
        print(response)
        fpw.write(p)
    except Exception as e:
        print(e)