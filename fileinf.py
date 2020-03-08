#Script Name      :fileinfo.py
#Author           :Not sure where I got this from
#Created          :28th November 2011
#Last Modified    :
#version          : 1.0

#Description      :show file information for a given file
#get file information using os.stat()
#tested with python24 vegsaeat 25sep2006
from __future__ import print_function 
import os
import stat
import sys
import time

if sys.version_info >=(3,0):
	raw_input =input
file_name=raw_input("Enter a file name")
count=0
t_char=0
try:
	with open(file_name) as f:
		line =f.readline()
		t_char+=len(line)
		while line:
			count+=1.0
			line=f.readline()
			t_char+=len(line)
except FileNotFoundError as e:
	print(e)
	sys.exit()
