from __future__ import division#division
import re
import urllib2

url = 'http://world.cankaoxiaoxi.com/2015/0404/730644.shtml'
html = urllib2.urlopen(url).read()
html = re.sub(r'<script[^>]*>([\s\S])*?</script[^>]*>','',html)#delete the script
html = re.sub(r'<style[^>]*>([\s\S])*?</style[^>]*>','',html)#delete the style
html = re.split("[\r\n]+",html)#split
for line in html:
	if line.strip()=='':
		continue
	line_sub = re.sub(r'<[^>]*>','',line)#record the words in a line
	if len(line_sub)/len(line) >= 0.5:#compare the text of the density
		if(line_sub.strip()!=''):
			print line_sub.strip()



