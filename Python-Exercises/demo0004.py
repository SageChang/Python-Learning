# 任一个英文的纯文本文件，统计其中的单词出现的个数。
import re
from collections import Counter
f = open(r'C:/Users/XYZH USER/Desktop/demo0004.txt', 'r')

word_list = []
line = f.readline()
while line:
	match = re.findall(r'[^a-zA-z0-9]+',line)
	for i in match:
		line = line.replace(i, ' ')
		line = line.lower()
	line_list = line.split()
	word_list.extend(line_list)
	line = f.readline()

word_count = Counter(word_list)

print(word_count)
