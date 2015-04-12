import urllib2
import urllib
import re

url = 'http://tieba.baidu.com/p/2166231880'
html = urllib2.urlopen(url).read()

photos = re.findall(r'class="BDE_Image" src="([^"]+)"',html)
i=0
for photo in photos:
	urllib.urlretrieve(photo,'C:/Users/zzl/Desktop/1/'+str(i)+'.jpg')
	i += 1

