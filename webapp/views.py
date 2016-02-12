from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound
from .form import RegistrationForm, LoginForm, PaymentForm
from sqlalchemy.exc import DBAPIError
from passlib.apps import custom_app_context as check_password
from .models import *
from .scripts.voucher import send_mail
from pyramid_mailer.message import Message
from pyramid_mailer.mailer import Mailer

from pyramid.view import (
    view_config,
    forbidden_view_config,
    )
from pyramid.security import (
    remember,
    forget,
    )

import hashlib
import time
import datetime
import json
from itsdangerous import JSONWebSignatureSerializer
from decimal import Decimal


itsden_signat = JSONWebSignatureSerializer('eyJhbGciOiJIUzUxMiJ9', algorithm_name='HS512')
mailer = Mailer()
RECIPIENTS = 'pavloshulga.95@gmail.com'
SUBJECT = 'Bundle'
SENDER = 'localhost'


@view_config(context=Exception)
def failed_view(exc, request):
    import traceback
    response = Response('Error, %s' % traceback.format_exc())
    response.status_int = 500
    return response


@view_config(route_name='preview', renderer='webapp:templates/preview.mako')
def preview(request):
    # user = DBSession.query(Users).filter_by(name=request.unauthenticated_userid).first()
    # order = DBSession.query(Orders).filter_by(mail=user.mail).first()
    # if order.id is not None:
    user = None
    if request.unauthenticated_userid is not None:
        user = DBSession.query(Users).filter_by(mail=request.unauthenticated_userid).first().id
    data = DBSession.query(Content).filter_by(id=request.matchdict['id']).first()
    return {'image': data.image,
            'title': data.title,
            'description': data.description,
            'link': None,
            'manufacture': data.manufacture,
            'user': user}


@view_config(route_name='bundle_preview', renderer='webapp:templates/bundle_preview.mako')
def bundle_preview(request):
    user = None
    if request.unauthenticated_userid is not None:
        user = DBSession.query(Users).filter_by(mail=request.unauthenticated_userid).first().id
    bundles = DBSession.query(Bundle).all()
    return {'items': bundles, 'user': user}


@view_config(route_name='content', renderer='webapp:templates/content.mako')
def content(request):
    try:
        dict_itsden = None
        user = None
        if request.unauthenticated_userid is not None:
            user = DBSession.query(Users).filter_by(mail=request.unauthenticated_userid).first().id
        data = DBSession.query(Content).filter_by(id=request.matchdict['id']).first()
        if data is not None:
            dict_itsden = itsden_signat.loads(request.cookies[str(data.bundle_id)])
        order = DBSession.query(Orders).filter(Orders.mail==dict_itsden['email'],
                                               Orders.bundle_id==dict_itsden['bundle_id']).first()
        _sum = DBSession.query(func.sum(Orders.sum_charity+Orders.sum_content)).\
            filter(Orders.bundle_id==dict_itsden['bundle_id'])
        if order is not None:
            get_content_by_id = DBSession.query(Content).filter(Content.id==request.matchdict['id'],
                                                                Content.tier<=_sum[0][0]).first()
            if get_content_by_id is not None:
                return {'image': get_content_by_id.image,
                        'title': get_content_by_id.title,
                        'description': get_content_by_id.description,
                        'link': get_content_by_id.link,
                        'manufacture': get_content_by_id.manufacture,
                        'user': user}
            else:
                return preview(request)
        else:
            return preview(request)
    except KeyError:
        return preview(request)


@view_config(route_name='index', renderer='webapp:templates/index.mako')
def index(request):
    user = None
    content_on_main = []
    _sum = lambda x: Decimal(x) if x is not None else Decimal(0)
    val = None
    _sold = None
    _bonus = []
    charity = None
    form = PaymentForm(request.POST)
    _bundle = DBSession.query(Bundle).all()
    if _bundle != []:
        _bundle = DBSession.query(Bundle).filter(Bundle.date_start<datetime.datetime.utcnow(),
                                                 Bundle.date_end>datetime.datetime.utcnow()).first()
        content_on_main = DBSession.query(Content).filter(Content.bundle_id==_bundle.id).\
            order_by(Content.tier).limit(4).all()
        _bonus = DBSession.query(Content).filter(Content.tier>=Decimal(25.00)).limit(2).all()
        charity = DBSession.query(Charity).filter_by(id=_bundle.charity_id).first()
        val = DBSession.query(func.sum(Orders.sum_charity)).filter(Orders.bundle_id==_bundle.id).all()

    if request.unauthenticated_userid is not None:
        user = DBSession.query(Users).filter_by(mail=request.unauthenticated_userid).first().id
    _sold = DBSession.query(func.count(Orders.id)).all()
    return {
        'items': content_on_main,
        'form': form,
        'total_raised': _sum((0 if val is None else val[0][0])),
        'sold': _sold[0][0],
        'bundle': _bundle,
        'bonus': _bonus,
        'charity': charity,
        'user': user
    }


@view_config(route_name='bundle', renderer='webapp:templates/bundle.mako')
def bundle(request):
    user = None
    if request.unauthenticated_userid is not None:
        user = DBSession.query(Users).filter_by(mail=request.unauthenticated_userid).first().id
    form = PaymentForm(request.POST)
    _bundle = DBSession.query(Bundle).filter_by(id=request.matchdict['id']).first()
    content_on_main = DBSession.query(Content).filter(Content.bundle_id==_bundle.id).\
        order_by(Content.tier).limit(4).all()
    _bonus = DBSession.query(Content).filter(Content.tier>=Decimal(25.00),
                                             Content.bundle_id==_bundle.id).limit(2).all()
    val = DBSession.query(func.sum(Orders.sum_charity)).filter(Orders.bundle_id==_bundle.id).all()
    _sum = lambda x: Decimal(x) if x is not None else Decimal(0)
    _sold = DBSession.query(func.count(Orders.id)).filter(Orders.bundle_id==_bundle.id).all()
    charity = DBSession.query(Charity).filter_by(id=_bundle.charity_id).first()
    response = {
            'items': content_on_main,
            'form': form,
            'total_raised': _sum(val[0][0]),
            'sold': _sold[0][0],
            '_bundle': _bundle,
            'bonus': _bonus,
            'charity': charity,
            'user': user
        }
    return response


@view_config(route_name='verify', renderer='webapp:templates/verify.mako')
def verify(request):
    code = request.matchdict['code']
    data = itsden_signat.loads(code)
    _bundle = DBSession.query(Bundle).filter_by(id=data['bundle_id']).first()
    response = Response()
    response.set_cookie(u'{}'.format(data['bundle_id']),
                        value=code, max_age=u'{}'.format(int(time.time()-_bundle.date_end.timestamp()) * -1 ))
    return HTTPFound(location=request.route_url('index'), headers=response.headers)


@view_config(route_name='login', renderer='webapp:templates/login.mako')
@forbidden_view_config(renderer='webapp:templates/login.mako')
def login(request):
    login_url = request.route_url('login')
    referrer = request.url
    if referrer == login_url:
        referrer = 'index' # never use the login form itself as came_from
    came_from = request.params.get('came_from', referrer)
    form = LoginForm(request.POST)
    message = 'Login'
    login = form.username.data
    password = form.password.data
    if request.method == 'POST' and login is not None and password is not None:
        db_query = DBSession.query(Users).filter(Users.mail == login).first()
        if db_query is not None:
            if db_query.mail == login and check_password.verify(password.encode('utf-8'), db_query.password):
                headers = remember(request, login)
                return HTTPFound(location=request.route_url('index'),
                                 headers=headers)
        message = 'Failed login'
    return {
            'message': message,
            'url': request.application_url + '/login',
            'came_from': came_from,
            'form': form,
    }


@view_config(route_name='logout', renderer='webapp:templates/logout.mako')
def logout(request):
    headers = forget(request)
    return HTTPFound(location=request.route_url('index'),
                     headers=headers)


@view_config(route_name='registration', renderer='webapp:templates/registration.mako')
def register(request):
    try:
        form = RegistrationForm(request.POST)
        try:
            if request.method == 'POST' and form.validate() and request.POST['reg_agree'] == 'on':
                new_user = Users()
                # new_user.name = form.username.data
                new_user.mail = form.email.data
                # new_user.sex = form.sex.data
                _hash = hashlib.sha224('{}'.format(time.time()).encode('utf-8')).hexdigest()
                # code = str(request.application_url + '/activate/{}'.format(_hash))
                # new_user.activate_code = code
                # try:
                #     send_mail(form.email.data, 'bundle', code)
                # except:
                #     pass
                if form.password.data.encode('utf8') == form.confirm_password.data.encode('utf8'):
                    new_user.set_password(form.password.data.encode('utf8'))
                DBSession.add(new_user)
                return HTTPFound(location=request.route_url('index'))
            return {'form': form, 'message': 'Register'}
        except:
            return {'form': form, 'message': 'Confirm the license'}
    except DBAPIError:
        return {'message': 'False'}


@view_config(route_name='account', renderer='webapp:templates/account.mako')
def user(request):
    if request.unauthenticated_userid is not None:
        user = DBSession.query(Users).filter_by(mail=request.unauthenticated_userid).first()
        user_order_history = DBSession.query(Orders, Bundle)
        records = user_order_history.join(Bundle, Bundle.id == Orders.bundle_id).filter(
                Orders.mail==request.unauthenticated_userid).order_by(Orders.timestamp).all()
        return {'user': user, 'query': records}

# @view_config(route_name='end_reg', renderer='webapp:templates/confirm.mako')
# def end_reg(request):
#     try:
#         db_query = DBSession.query(Users).filter(Users.activate_code == request.url).first()
#         if db_query.activate_code is not None:
#             if request.url == db_query.activate_code:
#                 DBSession.query(Users).filter_by(id=db_query.id).update({'is_active': True})
#                 return HTTPFound(location=request.route_url('index'))
#         return HTTPFound(location=request.route_url('index'))
#     except Exception as e:
#         print(e)
#     return {'message': 'You account is activate!'}


@view_config(route_name='about', renderer='webapp:templates/about.mako')
def about(request):
    user = None
    if request.unauthenticated_userid is not None:
        user = DBSession.query(Users).filter_by(mail=request.unauthenticated_userid).first().id
    return {'user': user}


@view_config(route_name='pay', renderer='webapp:templates/pay.mako')
def pay_methods(request):
    form = PaymentForm(request.POST)
    if request.method == 'POST':
        amount = request.POST['amount']
        content = request.POST['content']
        charity = request.POST['charity']
        email = request.POST['email']
        credit_card = form.card.data
        sum_content = float(amount) * float(content) / 100
        sum_charity = float(amount) * float(charity) / 100
        _bundle = DBSession.query(Bundle).filter(Bundle.date_start<=datetime.datetime.utcnow(),
                                                 Bundle.date_end>=datetime.datetime.utcnow()).first()
        codec = {
            'email': email,
            'card': credit_card,
            'charity': float(sum_charity),
            'content': float(sum_content),
            'amount': float(amount),
            'bundle_id': _bundle.id
        }
        res = itsden_signat.dumps(codec)
        if float(form.amount.data) >= 2.0:
            if (sum_charity+sum_content==float(amount)):
                code = request.application_url+'/verify/{}'.format(res.decode())
                # send_mail(email, 'You code', code)
                try:
                    message = Message(subject=SUBJECT,
                                  sender=SENDER,
                                  recipients=[RECIPIENTS],
                                  body='Your link {}'.format(code))
                    mailer.send(message)
                except Exception as e:
                    print(e)
                new_order = Orders(sum_charity=sum_charity, sum_content=sum_content, mail=email,
                                   bundle_id=codec['bundle_id'])
                DBSession.add(new_order)
                print(code)
                # if DBSession.query(Users).filter_by(mail=email).first() is None:
                #     new_user = Users()
                #     new_user.mail = email
                #     DBSession.add(new_user)
                return HTTPFound(location="/")
            else:
                return {'message': 'Bundle is not exist or sum content + sum charity != amount'}
        else:
            return {'message': 'Enter sum >= 2'}


@view_config(route_name='b_content', renderer='webapp:templates/bonus.mako')
def bonus_content(request):
    try:
        # if request.unauthenticated_userid is not None:
        user = None
        if request.unauthenticated_userid is not None:
            user = DBSession.query(Users).filter_by(mail=request.unauthenticated_userid).first().id
        dict_itsden = itsden_signat.loads(request.cookies['info'])
        order = DBSession.query(Orders).filter_by(mail=dict_itsden['email']).first()
        _sum = DBSession.query(func.sum(Orders.sum_charity+Orders.sum_content)).filter(Orders.mail==dict_itsden['email'])
        if order is not None:
            get_content_by_id = DBSession.query(Content).filter(Content.id==request.matchdict['id'],
                                                                Content.tier<=_sum[0][0]).first()
            if get_content_by_id is not None:
                return {'image': '../'+get_content_by_id.image,
                        'title': get_content_by_id.title,
                        'description': get_content_by_id.description,
                        'link': get_content_by_id.link,
                        'manufacture': get_content_by_id.manufacture,
                        'user': user}
            else:
                return preview(request)
        else:
            return preview(request)
        # else:
        #     return preview(request)
    except KeyError:
        return HTTPFound(location='/')
