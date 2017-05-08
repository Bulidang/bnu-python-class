# 第一步，获取物理系网页师资队伍所有老师的照片，并下载到本地
import requests, re, os
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont


def get_bsobj(web_url):
    """获得网址的BeautifulSoup对象(解决乱码)"""
    html = requests.get(web_url)
    html.encoding = 'gb2312'
    bsobj = BeautifulSoup(html.text, 'html.parser')
    return bsobj

# 获得表格链接
url = 'http://physics.bnu.edu.cn/application/faculty/faculty_left.php'
soup = get_bsobj(url)
r = re.findall(r'/.*.php', str(soup))
for i in r[1:6]:
    table_url = os.path.dirname(url) + i
    # 对表格分析
    soup2 = get_bsobj(table_url)
    for j in soup2.select('tr td a'):
        # 获得老师名字和个人主页链接
        if j['href'].startswith('./'):
            teacher_name = j.text.strip()
            teacher_url = os.path.dirname(table_url) + j['href'][1:]
            # 获取图片链接，并保存为jpg
            obj = get_bsobj(teacher_url)
            tag = obj.find('img', border='0')
            if tag and tag.get('src').startswith('./'):
                image_url = os.path.dirname(teacher_url) + tag.get('src')[1:]
                with open(r'{}.jpg'.format(teacher_name), 'wb') as f:
                    f.write(requests.get(image_url).content)

# 第二步，拼接图像
# 共55张,6行9列放置,图片左右间隔10，上下间隔50, 图片大小设为
# width = 160, height = 200
new_im = Image.new('RGB', (170*9+10, 250*6+10), 'white')
draw = ImageDraw.Draw(new_im)
x = y = 10
for filename in os.listdir('.'):
    if not filename.endswith('.jpg'):
        continue
    im = Image.open(filename).resize((160, 200))
    new_im.paste(im, (x, y))
    draw.text((x + 35, y + 200), filename[:-4], fill='purple', font=ImageFont.truetype('msyhl.ttc', 30))
    x += 170
    if x+160 > 170*9+10:
        x, y = (10, y + 250)

new_im.save('together.jpg')






