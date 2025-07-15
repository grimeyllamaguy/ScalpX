import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_gmail_alert(symbol, price, signal):
    sender_email = 'YOUR_GMAIL_EMAIL'
    receiver_email = 'RECIPIENT_EMAIL'
    password = 'YOUR_GMAIL_APP_PASSWORD'

    # Create the email content
    subject = f"Trade Signal Alert for {symbol}"
    body = f"Symbol: {symbol}\nPrice: ${price}\nSignal: {signal}"
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Connect to Gmail SMTP server and send email
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.close()
        print(f"Gmail alert sent successfully to {receiver_email}")
    except Exception as e:
        print(f"Failed to send Gmail alert: {e}")
