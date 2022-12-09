import smtplib
from datetime import datetime
import time

# email settings
smtp_server = "smtp.gmail.com"
port = 587
sender = "sender@gmail.com"
password = "********"
recipient = "recipient@gmail.com"

# message settings
subject = "Notification"
body = "This is a notification email sent on a schedule"
message = f"Subject: {subject}\n\n{body}"

# schedule settings (send email every hour)
interval = 3600

while True:
    # check if it's time to send the email
    now = datetime.now()
    if now.minute == 0 and now.second == 0:
        # connect to the SMTP server
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender, password)

        # send the email
        server.sendmail(sender, recipient, message)

        # disconnect from the SMTP server
        server.quit()

    # wait for the next interval
    time.sleep(interval)
