from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont
import requests, os

# 第一步：下载学院老师图片到本地
url = 'http://psych.bnu.edu.cn/tabid/50/Default.aspx'
html = requests.get(url)
bsobj = BeautifulSoup(html.content, 'html.parser')

for i in bsobj.select('li img'):
    img_url = 'http://psych.bnu.edu.cn' + i['src']
    name = i.parent.next_sibling.next_sibling.text.strip()  # 获得老师名字
    img = requests.get(img_url)
    with open('{}.jpg'.format(name), 'wb') as f:
        f.write(img.content)


# 第二步：拼接图片
# 共56张图片，7行8列放置,图片大小为
width = 260*7 // 10
height = 320*7 // 10
# 图片左右间隔10，上下间隔50
new_im = Image.new('RGB', (width*8+90, height*7+320), 'white')  # 创建空白图片
draw = ImageDraw.Draw(new_im)

x = y = 10
for filename in os.listdir('.'):
    if not filename.endswith('.jpg'):
        continue
    im = Image.open(filename).resize((width, height))
    new_im.paste(im, (x, y))    # 将老师图片粘贴在空白图片上
    draw.text((x+width//4, y+height), filename[:-4], fill='purple',
              font=ImageFont.truetype('msyhl.ttc', 30))
    x += width+10
    if x > width*8+90:
        x = 10
        y += height+50

new_im.save('together.jpg')
