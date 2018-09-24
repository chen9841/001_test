import requests
import re

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
url = "http://s.dianping.com/topic/38302339?utm_source=forum_pc_index"


response = requests.get(url, headers=headers)
# print(response)
src_link = re.findall(r'img data-lazyload="(.*?)"', response.text, re.S)
for src in src_link:
	print(src)
	#pic = requests.get(src, headers=headers).content

	#filename = src[-20:-10]
	#file = "./"+filename+".jpg"

	#with open(file, "wb") as f:
	#	f.write(pic)
