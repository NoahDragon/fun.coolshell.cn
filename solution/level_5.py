import urllib.request
url = 'http://fun.coolshell.cn/n/'
num = '2014' 
while(True):
	full_url = url + num
	print(full_url)
	html = urllib.request.urlopen(full_url)
	num = html.read().decode("utf-8") # to transform bytes to str in python 3
	html.close()

