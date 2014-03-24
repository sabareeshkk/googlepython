#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""



def read_urls(filename):
	img_url =[]
	path = open(filename).read()
        match = re.findall(r'GET (\S+.jpg) HTTP/1.0',path)
	#match.pop()
	#return match
	sername = re.match(r'animal_(\w+.\w+.\w+)',filename)
	#return sernam.group(1)
	for matches in match:
		img_url.append("http://"+sername.group(1)+matches)
	img_ur=set(img_url)
	img_urls = sorted([imge for imge in img_ur ])
	return img_urls
def download_images(img_urls, dest_dir):
	if not os.path.exists(dest_dir):
		os.mkdir(dest_dir)
	index = file(os.path.join(dest_dir,'index.html'),'w')
	index.write('<html><body>\n')
	k=0
	for img in img_urls:
		name_file = 'img%d' % k
		urllib.urlretrieve(img,os.path.join(dest_dir,name_file))	
		index.write('<img src="%s">' % (name_file,))
		k += 1
	index.write('\n</body></html>\n')
	index.close()
def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
