#!/usr/bin/python3
# scripted by CDnX

import codecs
import sys

if len(sys.argv) != 2:
	errorstr = "Number of arguments needs to be 1, but %d given"%(len(sys.argv)-1,)
	raise ValueError(errorstr)
else:
	with open(sys.argv[1], "r") as fi, open(sys.argv[1]+".yml", "w") as fo:
		lines = fi.readlines()
		fo.write("\ufeffl_english:\n")
		fo.writelines([" " + line.replace("코0=", ":0 ", 1).replace("<?>", "") for line in lines])
