import sys
import os
import datetime
import smtplib
from email import charset
from email import encoders, utils
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
import mimetypes

SMTPSERVER = '127.0.0.1'
FROM_ADDR='foo@bar.local'
FROM_NAME='foobar'

def create_attachment_file(filename):
	fd = open(filename, 'rb')
	mimetype, mimeencoding = mimetypes.guess_type(filename)
	if mimeencoding or (mimetype is None):
		mimetype = 'application/octet-stream'
	
	maintype, subtype = mimetype.split('/')
    
	if maintype == 'text':
		retval = MIMEText(fd.read(), _subtype=subtype)
	else:
		retval = MIMEBase(maintype, subtype)
		retval.set_payload(fd.read())
		encoders.encode_base64(retval)
		
	cset = 'utf-8'
	#retval.add_header('Content-Disposition', 'attachment', filename=Header(filename,cset))
	retval.add_header('Content-Disposition', 'attachment', filename=filename)
	fd.close()
	return retval


def create_message(toaddr,subject,message,files,from_name, from_addr):
	msg = MIMEMultipart()
	cset = 'utf-8'# <---------------(文字セットの設定)#cset = 'iso-2022-jp'
	
	msg['Subject'] = Header(subject, cset)
	msg['From'] = Header(from_name,cset)
	msg['From'].append(' <'+from_addr+'>','ascii')
	msg['To'] = toaddr
	
	body = MIMEText(message, 'plain', cset)
	msg.attach(body)
	
	for filename in files:
		obj = create_attachment_file(filename)
		msg.attach(obj)
	
	return msg


def sendmail(tolist,subject,msg, files=[], from_name=FROM_NAME, from_addr=FROM_ADDR, smtpserver=SMTPSERVER):
	con = smtplib.SMTP(smtpserver)
	con.set_debuglevel(True)
	
	#toaddr = 'ishida-t@city.obama.lg.jp'
	toaddr = ",".join(tolist)
	message = create_message(toaddr, subject, msg, files, from_name, from_addr)	
	con.sendmail(from_addr, tolist, message.as_string())
	con.close()
	return


#sendmail('aaa',"test","good!",['e-Nais予定表2018-06.xlsx'])