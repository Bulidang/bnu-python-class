import requests
from bs4 import BeautifulSoup
# 在windows下面，新文件的默认编码是gbk，
# 这样的话，python解释器会用gbk编码去解析我们的网络数据流txt，
# 然而txt此时已经是decode过的unicode编码，
# 这样的话就会导致解析不了，出现上述问题。
# 解决的办法就是，改变目标文件的编码：


with open('title.txt', 'w', encoding='utf-8') as f:
    url = 'http://www.bnu.edu.cn/bsdkx/index.html'
    for num in range(1, 5):
        html = requests.get(url)
        bs = BeautifulSoup(html.content, "html.parser")
        for i in bs.select('a[title]'):
            time = i.next_sibling.next_sibling.text
            if time[:7] == '2017-04':
                f.write(time + i.get('title').strip() + '\n')
        url = 'http://www.bnu.edu.cn/bsdkx/index{}.html'.format(num)



