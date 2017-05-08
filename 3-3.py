# 获取每个搜索结果的对应的品牌和价格，统计每种品牌的平均价、最高价和最低价
# 在京东上搜索“笔记本电脑15.6寸”
import requests
from bs4 import BeautifulSoup


lst = '联想 戴尔 神舟 惠普 华硕 微星 炫龙 雷神'.split(' ')
brands = {k: v for k, v in zip(lst, [[] for i in range(9)])}
# brands = {'小米': [], '联想': [], '华硕': [], '惠普': [], '戴尔': [], 'Apple': []}

for i in range(1, 10, 2):
    url = 'https://search.jd.com/Search?keyword=笔记本电脑\
    15.6寸&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&offset=3&suggest=1.def.0.T11&page={}'.format(i)
    html = requests.get(url)
    obj = BeautifulSoup(html.content, 'html.parser')
    a = obj.find_all('div', class_='gl-i-wrap')
    for j in a:
        t = j.select('em')
        if len(t) == 2:
            value, brand = t[0].next_sibling.next, t[1].next_element
            if float(value) < 1000:
                continue
            # print('价格：{}   品牌：{}'.format(value, brand))
            for key in lst:
                if key in brand:
                    brands[key] += [float(value)]
# print(brands)

# 对字典brands 的操作，统计每种品牌的平均价、最高价和最低价
for k in brands:
    v_lst = brands[k]
    print('{:^7}:  平均价:{:^10.2f},最高价:{:^10},最低价:{:^10}'.format(
           k, sum(v_lst) / len(v_lst), max(v_lst), min(v_lst)))


