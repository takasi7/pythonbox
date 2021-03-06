#! /usr/local/bin/python3

import argparse
def getarg():
	parser = argparse.ArgumentParser()
	parser.add_argument("-u","--unverified",help="no verify certificate",     action="store_true" )
	parser.add_argument("-H","--headers",   help="set http headers",          action="append"     )
	parser.add_argument("-p","--prefix",    help="specify prefix",            default=''          )
	parser.add_argument("-r","--referer",   help="set referer header"                             )
	parser.add_argument("-e","--end",       help="specify end url line",       type=int,default=-1)
	parser.add_argument("m3u8file",         help="m3u8 file must be specified."                   )
	args = parser.parse_args()
	return args
	
import ssl
def ssl_unverified():
	ssl._create_default_https_context = ssl._create_unverified_context
	

import urllib.request
import urllib.error
def http_download(url,headers={"Accept":"*/*","Connection":"keep-alive"},outputpath="download_file"):
	req = urllib.request.Request(url, headers=headers)
	try:
		with urllib.request.urlopen(req) as res:
			body = res.read()
			f = open(outputpath,"wb")
			f.write(body)
			f.close()
	except urllib.error.HTTPError as e:
		if e.code >= 400:
			print (e.reason)
			return -1
		else:
			raise e
	
	return 0

import subprocess
def command_shell(cmd='echo "hello,world"'):
	subprocess.call(cmd,shell=True)


import codecs
def split_csv(string):
	string = string.replace('\r','')
	string = string.replace('\n','')
	rec = []
	item = ''
	mode = 0
	for c in string:
		if c == '"' and mode == 0:
			mode=1
			continue
		elif c == '"' and mode == 1:
			mode=0
			continue
			
		if c == ',' and mode == 0:
			rec.append(item)
			item = ''
		else:
			item += c
	
	if len(item):
		rec.append(item)
		
	return rec
	

def load_data(file,encoding='utf-8'):
	records=[]
	fh = codecs.open(file, mode='r', encoding=encoding)
	line = fh.readline()
	while line:
		rec = split_csv(line)
		records.append(rec)
		line=fh.readline()
		
	return records

if __name__ == '__main__':
	cmd = 'echo "hello,world"'
	subprocess.call(cmd,shell=True)
