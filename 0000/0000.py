
"""
第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果
"""

from PIL import Image,ImageDraw,ImageFont

number = str(666)
color = (255,255,255)
windows_font= 'GOUDOSB.ttf'

def draw_text(text,fill_color,windows_font):
    im = Image.open('Tianchi.jpg')
    x,y = im.size
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(windows_font,200)
    draw.text((x-300,30),text,fill_color,font)

    im.save('Tianchi1.jpg')

draw_text(number,color,windows_font)

