# send email 17

def send_em(useremail):
	# Import smtplib for the actual sending function
	import smtplib


	# Import the email modules we'll need
	from email.mime.text import MIMEText

	# Here are the email package modules we'll need
	from email.mime.image import MIMEImage
	from email.mime.multipart import MIMEMultipart

	# Open a plain text file for reading.  For this example, assume that
	# the text file contains only ASCII characters.
	#with open('abc') as fp:
    # Create a text/plain message
    #msg = MIMEText(fp.read())

    # Create the container (outer) email message.
	msg = MIMEMultipart()
	msg['Subject'] = 'YOUR PHOTO <3'

	# me == the sender's email address
	# you == the recipient's email address
	msg['From'] = "cyberbrushsfhacks@gmail"
	msg['To'] = useremail # string
	msg.preamble = 'filtered photo'

	from os import listdir
	from os.path import isfile, join
	onlyfiles = [f for f in listdir("photo/HK")] # photo dir

	for file in onlyfiles:

        # Open the files in binary mode.  Let the MIMEImage class automatically
        # guess the specific image type.
    	with open('photo/HK/' + file, 'rb') as fp: # photo dir
        img = MIMEImage(fp.read())
		msg.attach(img)

    # Send the message via our own SMTP server.
	s = smtplib.SMTP('smtp.gmail.com',587)
	s.starttls()
	s.login('cyberbrushsfhacks@gmail.com', 'cyberbrus')
	s.send_message(msg)
	s.quit()

	return
