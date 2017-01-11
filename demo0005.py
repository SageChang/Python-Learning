# 第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

from PIL import Image
import glob, os
for infile in glob.glob("C:/Users/XYZH USER/Desktop/plots/*"): # 打开绝对路径下的所有文件，也可写成“plots/*.jpes”寻找特殊扩展名文件
	file, ext = os.path.splitext(infile) # 获取文件名称
	im = Image.open(infile) # 打开图片
	im = im.resize((3264,2488)) # 调整图片分辨率
	im.save(file + "-IPhone5.JPEG", "JPEG") # 保存为文件名+后缀的新图片文件