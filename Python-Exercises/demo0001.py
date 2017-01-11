# 第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？

import random
str = ''
list_1 = []
for i in range(97,123):
	list_1.append(chr(i))
for j in range(48,57):
	list_1.append(chr(j))
for k in range(65,90):
	list_1.append(chr(k))
str = str.join(list_1)
series_set_final = []

def random_series(len = 10):
	series = ''
	series_set = []	
	for i in range(0, len):
		series += random.choice(str)
		if series not in series_set:
			series_set.append(series)
	series_set_final.append(series_set[-1])

for i in range(0,200):
	random_series()
print(series_set_final)

