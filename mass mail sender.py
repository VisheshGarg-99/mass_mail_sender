import pandas as pd 
import smtplib
from email.message import EmailMessage

data = pd.read_excel(<path of excel file>) #---------enter the path of excel file
emails = data.get('emails') #-------column name in which emails ids are present for me it is emails
lis = list(emails)


def ids():
	i=1
	for l in lis:
		to = l
		server.sendmail(from_ , to , str(msg)) 
		print(str(i) + '. sent')
		i+=1 

server = smtplib.SMTP("smtp.gmail.com", '587')
server.starttls()
server.login( "<sender email id>", "<password>") #--------sender email id and password
from_ = "<sender name>" #---------sender name


msg = EmailMessage()
msg['Subject'] = '<subject of mail>' #------enter the subject of mail
msg['from'] = "<sender name>" #--------sender name
with open('<path of mail template file like txt >') as f: #-------mail template
	r = f.read()
	msg.set_content(r)

with open(<path of add_attachment file>, 'rb') as p: #---------attachment file
	file_data = p.read()
	file_name = p.name
	msg.add_attachment(file_data, maintype = "application" , subtype = 'pdf' , filename = file_name)

ids()
print('done')



