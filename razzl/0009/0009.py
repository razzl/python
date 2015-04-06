import re
import urllib2

url = 'http://www.cnblogs.com/jasondan/p/3497757.html'
html = urllib2.urlopen(url).read()
links = re.findall(r'<[^>]+src="([^>]+)"[^>]*>|<[^>]+href="([^>]+)"[^>]*>',html)#find the link
for link in links:
	for lin in link:
		print lin
