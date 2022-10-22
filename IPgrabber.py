import smtplib, ssl
import ip_address as ip


address = ip.get()

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "someone@gmail.com"  # Enter your address
receiver_email = "someone@gmail.com"  # Enter receiver address
password = "App Password from Google" # Enter your Google App Password
message = "This is the IP from the link: " + address

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)