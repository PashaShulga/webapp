from pyramid_mailer.message import Message
from pyramid_mailer.mailer import Mailer
from itsdangerous import TimestampSigner

__all__ = ['send_mail']


def send_mail(request, body, sender):
    mailer = Mailer()
    message = Message(subject=request['subject'], recipients=request['recipient'], body=body, sender=sender)
    mailer.send(message)


def _voucher(string, secret):
    s = TimestampSigner(secret)
    res = s.sign(string)
    print(res)


