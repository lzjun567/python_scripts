from urllib import request
from bs4 import BeautifulSoup

fp = open('host.txt', 'w')
for i in range(1,3):
    url='http://www.xicidaili.com/wn/' + str(i)
    opener=request.build_opener()
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    request.install_opener(opener)
    response = request.urlopen(url)
    soup = BeautifulSoup(response.read(),'html.parser')
    list = soup.find_all(class_='odd')
    for elem in list:
        data = elem.find_all('td')
        ip=data[1].string
        port=data[2].string
        fp.write(ip)
        fp.write('\t')
        fp.write(port)
        fp.write('\n')
fp.close()
