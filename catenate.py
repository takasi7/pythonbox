#! /usr/local/bin/python3
import re
import os
import subprocess

def geninput(files):
	f = open('input.txt','w')
	for fn in files:
		f.write("file " + fn + '\n')
	f.close()

def catenatefile(serdic):
	cmd = 'ffmpeg -f concat -safe 0 -i input.txt -c copy OUTPUTFILE'
	for key in serdic.keys():
		val = serdic[key]
		geninput(val)
		(root, ext) = os.path.splitext(val[0])
		ffmpeg = cmd.replace('OUTPUTFILE', key + ext)
		subprocess.call(ffmpeg)
		#print(ffmpeg)

def findserialized(filelist):
	retdic = {}
	filelist.sort()
	for f in filelist:
		r = f.split('@')
		if len(r) == 1:
			continue
		
		if r[0] not in retdic:
			retdic[r[0]] = []
			
		retdic[r[0]].append(f)
	
	for key in retdic.keys():
		val = retdic[key]
		if len(val) <= 1:
			del retdic[key]
			
	return retdic

def catenate(path='.'):
	files = os.listdir(path)
	files_file = [f for f in files if os.path.isfile(os.path.join(path, f))]
	dic = findserialized(files_file)
	catenatefile(dic)

if __name__ == '__main__':
	catenate()
