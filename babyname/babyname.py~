import urllib
import sys
import re
def url(u):
	a = []
	ufile = urllib.urlopen(u)
	text = ufile.read()
	match = re.search(r'Popularity\sin\s(\d\d\d\d)',text)
	if match:
		 a.append(match.group(1))
	rank = re.findall(r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>',text)
	for i,j,k in rank:
		a.append(j+ " " + i)
		a.append(k+ " " + i)
	a.sort()
	print a
	for m in a:
		print m	
url(sys.argv[1])

