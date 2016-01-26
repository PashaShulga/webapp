# from pyramid_mailer.message import Message
# from pyramid_mailer.mailer import Mailer
from itsdangerous import JSONWebSignatureSerializer, Signer
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

SMTP_USER = u'pavloshulga.95@gmail.com'
SMTP_PASS = u'Reload_777'
ENCODING = 'utf-8'


def send_mail(email_to, subj, text, email_from='pavloshulga.95@gmail.com'):
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


def voucher():
    test_dict = {
        'email': 'lol@lol.com',
        'card': '123456789012345678901234567890',
        'charity': 20,
        'content': 80,
        'amount': 25
                }
    s = JSONWebSignatureSerializer('secret', algorithm_name='HS512')
    res = s.dumps(test_dict)
    print(res)
    l = s.loads(res)
    print(l)


# voucher()