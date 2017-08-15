# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

class email:
    def __init__(self, username, password):
	# me == the sender's email address
	self.me = '{}@gmail.com'.format(username)
        # setup connection with server
	self.setup(username, password)
   
    def setup(self, username, password):
	self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
	self.server.login(username, password)
   
    def sendmail(self, subj, msg, to_addr_list):
	server = self.server
	# Create a text/plain message
	msg = MIMEText(msg)
	
	# you == the recipient's email address
	msg['Subject'] = subj 
	msg['From'] = self.me 
	msg['To'] = ','.join(to_addr_list) 
	server.sendmail(self.me, to_addr_list, msg.as_string())

    def teardown(self):
	self.server.quit()

#Test code
if __name__ == '__main__':
    mail = email('pybot8055', 'AI@pie/3.14')
    mail.sendmail('subject', 'content', ['jayadev.e3@gmail.com'])
    mail.teardown()
