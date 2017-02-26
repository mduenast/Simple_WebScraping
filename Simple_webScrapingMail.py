import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

fromaddr = "YOUR ADDRESS"
password ="YOUR PASSWORD"
toaddr = "ADDRESS YOU WANT TO SEND TO"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "SUBJECT OF THE MAIL"

body = "YOUR MESSAGE HERE"
msg.attach(MIMEText(body, 'plain'))

smtp_server = 'smtp.gmail.com' # default
smtp_port = 587 # default

server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(fromaddr, )
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()