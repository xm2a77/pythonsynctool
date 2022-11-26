import requests
from bs4 import BeautifulSoup

sync_list = []

ip_address = input('IP:')

page_list = requests.get('http://'+ip_address).text
#print(page_list)

soup = BeautifulSoup(page_list, 'html.parser')
#print(type(soup))
for i in soup.find_all(name='a'):
    #print(i)
    sync_list.append(i.string)


for i in range(len(sync_list)):
    print('正在同步:'+sync_list[i])
    try:
        file_address = 'http://' + ip_address + '/' + sync_list[i]
        #print(file_address)
        file = requests.get(file_address)
        #print(file.text)
        f = open(sync_list[i], "wb")
        f.write(file.content)
        f.close
        print(sync_list[i],'同步完成!')
    except:
        print('同步失败：'+sync_list[i])