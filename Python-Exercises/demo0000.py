# 第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果

from PIL import Image
from pylab import *

im = array(Image.open('C:/Users/Adam/Desktop/o_me.jpg'))
imshow(im)
x = 0
plt.text(170, 10, '3', wrap=True, color = 'r', weight = 100, size = 20, stretch = 'extra-expanded')

show()