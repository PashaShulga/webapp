# from pyramid_mailer.message import Message
# from pyramid_mailer.mailer import Mailer
from itsdangerous import TimestampSigner
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

SMTP_USER = 'pavloshulga.95@gmail.com'
SMTP_PASS = 'Reload_777'
ENCODING = 'utf-8'


def send_mail(email_from, email_to, subj, text):
    _msg = MIMEMultipart()
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    _msg['from'] = Header(email_from, ENCODING)
    _msg['to'] = Header(email_to, ENCODING)
    _msg['subject'] = Header(subj, ENCODING)
    _msg_text = MIMEText(text.encode(ENCODING), 'plain', ENCODING)
    _msg_text.set_charset(ENCODING)
    _msg.attach(_msg_text)
    try:
        server.ehlo()
        server.login(SMTP_USER, SMTP_PASS)
    except smtplib.SMTPAuthenticationError as e:
        print(e)
    try:
        server.sendmail(email_from, email_to, _msg.as_string())
    except smtplib.SMTPException as e:
        print(e)
    finally:
        server.quit()


def voucher(string, secret):
    s = TimestampSigner(secret)
    res = s.sign(string)
    return res
