
# Python code to illustrate Sending mail from
# your Gmail account
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login('harshjarsh123@gmail.com', 'Harsh@123')

# message to be sent
message = "Message_you_need_to_send"

# Step 2 : Creating the message

msg = MIMEMultipart()
msg['From'] = 'Starlord'
msg['To'] = 'harshduolivre@gmail.com'
msg['Subject'] = 'Just a Test'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))


# Step 3 : Attaching an image

filename = 'kakashi.png'

attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()

# sending the mail
s.sendmail("harshjarsh123@gmail.com", "harshduolivre@gmail.com", text)

# terminating the session
s.quit()



