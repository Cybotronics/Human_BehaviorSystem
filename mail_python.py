import smtplib
 
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
 
def jump_mail():
	fromaddr = "yourmail@mail.com"
	toaddr = "TOSEND@mail.com"
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "SUBJECT OF THE MAIL"
 
	body = "object jumping"
	msg.attach(MIMEText(body, 'plain'))
 
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, "yourmailpassword")
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	print "mail sent successfully"
	server.quit()
def fall_mail():
	fromaddr = ""
	toaddr = ""
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "SUBJECT OF THE MAIL"
 
	body = "object falls"
	msg.attach(MIMEText(body, 'plain'))
 
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, "your password")
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	print "mail sent successfully"
	server.quit()
		
def running_mail():
	fromaddr = ""
	toaddr = ""
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "SUBJECT OF THE MAIL"
 
	body = "object running"
	msg.attach(MIMEText(body, 'plain'))
 
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, "your password")
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	print "mail sent successfully"
	server.quit()
