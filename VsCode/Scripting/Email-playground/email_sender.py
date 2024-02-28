import smtplib
from email.message import EmailMessage 
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'GauravKrThakur'
email['to'] = 'mandeepyadav3000@gmail.com'
email['subject'] = 'Hehe i did it !!!'

email.set_content(html.substitute({'name' :"Demon"}), 'html')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('gauravkrthakur007@gmail.com','umkryhrijizctkhz')       # in Place of Email and Password write you real email and password
    smtp.send_message(email)
    print("All Done!")


