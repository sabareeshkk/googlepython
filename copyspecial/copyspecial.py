#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands
def get_special_paths(dirname):
	paths=[]
	filenames = os.listdir(dirname)
	for filename in filenames:
		if re.search(r'__\w+__',filename):
			paths.append(os.path.abspath(os.path.join(dirname,filename)))
	print paths
def copy_to(filenames,to_dir):
	if not os.path.exists(to_dir):
		os.mkdir(to_dir)
	for filename in filenames:
		files = os.path.basename(filename)
		shutil.copy(filename,os.path.join(to_dir,files))
def zip_to(filenames,zipfile):
	cmd = 'zip -j ' + zipfile + ' ' + ' '.join(filenames)
	print "Command I'm going to do:" + cmd
	(status, output) = commands.getstatusoutput(cmd)
	if status:
		sys.stderr.write(output)
		sys.exit(1)

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)
  paths = []
  for dirname in args:
    paths.extend(get_special_paths(dirname))

  if todir:
    	copy_to(paths, todir)
  elif tozip:
    	zip_to(paths, tozip)
  else:
    	print '\n'.join(paths)
  
if __name__ == "__main__":
  main()
