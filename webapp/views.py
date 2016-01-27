from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound
from .form import RegistrationForm, LoginForm, PaymentForm
from sqlalchemy.exc import DBAPIError
from passlib.apps import custom_app_context as check_password
from .models import *
from .scripts.voucher import send_mail

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
from itsdangerous import JSONWebSignatureSerializer


itsden_signat = JSONWebSignatureSerializer('eyJhbGciOiJIUzUxMiJ9', algorithm_name='HS512')


def users_check(func):
    def wrapper(user_name):
        if user_name is not None:
            query = DBSession.query(Users).filter(Users.name == user_name).first()
            if query.is_active:
                func()
                return True


@view_config(route_name='preview', renderer='webapp:templates/preview.mako')
def preview(request):
    try:
        # user = DBSession.query(Users).filter_by(name=request.unauthenticated_userid).first()
        # order = DBSession.query(Orders).filter_by(mail=user.mail).first()
        # if order.id is not None:
        data = DBSession.query(Content).filter_by(id=request.matchdict['id']).first()
        return {'image': '../'+data.image,
                    'title': data.title,
                    'description': data.description,
                    'link': None,
                    'manufacture': data.manufacture}
    except DBAPIError:
        return HTTPFound(location='/')


@view_config(route_name='preview_bundle', renderer='webapp:templates/preview_bundle.mako')
def preview_bundle(request):
    try:
        bundles = DBSession.query(Bundle).all()
        return {'items': bundles}
    except Exception as e:
        print(e)

    return {}



@view_config(route_name='content', renderer='webapp:templates/content.mako')
def content(request):
    try:
        dict_itsden = itsden_signat.loads(request.cookies['info'])
        order = DBSession.query(Orders).filter_by(mail=dict_itsden['email']).first()
        _sum = DBSession.query(func.sum(Orders.sum_charity+Orders.sum_content)).filter(Orders.mail==dict_itsden['email'])
        if order is not None:
            get_content_by_id = DBSession.query(Content).filter(Content.id==request.matchdict['id'],Content.tier<=_sum[0][0]).first()
            if get_content_by_id is not None:
                return {'image': '../'+get_content_by_id.image,
                        'title': get_content_by_id.title,
                        'description': get_content_by_id.description,
                        'link': get_content_by_id.link,
                        'manufacture': get_content_by_id.manufacture}
            else:
                return preview(request)
        else:
            return preview(request)
    except KeyError:
        return preview(request)


@view_config(route_name='index', renderer='webapp:templates/index.mako')
def index(request):
    try:
        form = PaymentForm(request.POST)
        content_on_main = DBSession.query(Content).order_by(Content.tier).limit(4).all()
        _bonus = DBSession.query(Content).filter(Content.tier>=float(25.00)).limit(2).all()
        bundle = DBSession.query(Bundle).filter(Bundle.date_end>datetime.datetime.utcnow(),
                                                Bundle.date_start<datetime.datetime.utcnow()).first()
        _sum = DBSession.query(func.sum(Orders.sum_charity)).all()
        _sold = DBSession.query(func.count(Orders.id)).all()
        return {'items': content_on_main,
                'form': form,
                'req': request.unauthenticated_userid,
                'link': '/logout',
                'total_raised': _sum[0][0],
                'sold': _sold[0][0],
                'bundle': bundle,
                'bonus': _bonus
            }
    except DBAPIError:
        return HTTPFound(location='/')


@view_config(route_name='bundle', renderer='webapp:templates/bundle.mako')
def bundle(request):
    try:
        form = PaymentForm(request.POST)
        bundle = DBSession.query(Bundle).filter_by(id=request.matchdict['id']).first()
        content_on_main = DBSession.query(Content).filter(Content.bundle_id==bundle.id).order_by(Content.tier).limit(4).all()
        _bonus = DBSession.query(Content).filter(Content.tier>=float(25.00), Content.bundle_id==bundle.id).limit(2).all()
        _sum = DBSession.query(func.sum(Orders.sum_charity)).all()
        _sold = DBSession.query(func.count(Orders.id)).all()
        return {'items': content_on_main,
                'form': form,
                'req': request.unauthenticated_userid,
                'link': '/logout',
                'total_raised': _sum[0][0],
                'sold': _sold[0][0],
                'bundle': bundle,
                'bonus': _bonus
            }
    except AttributeError:
        return HTTPFound(location='/')


# @view_config(route_name='login', renderer='webapp:templates/login.mako')
# @forbidden_view_config(renderer='webapp:templates/login.mako')
# def login(request):
#     login_url = request.route_url('login')
#     referrer = request.url
#     if referrer == login_url:
#         referrer = 'index' # never use the login form itself as came_from
#     came_from = request.params.get('came_from', referrer)
#     form = LoginForm(request.POST)
#     message = 'Login'
#     login = form.username.data
#     password = form.password.data
#
#     if request.method == 'POST' and login is not None and password is not None:
#         db_query = DBSession.query(Users).filter(Users.name == login).first()
#         if db_query is not None:
#             if db_query.name == login and check_password.verify(password.encode('utf-8'), db_query.password):
#                 headers = remember(request, login)
#                 return HTTPFound(location=request.route_url('index'),
#                                  headers=headers)
#         message = 'Failed login'
#
#     return {
#             'message': message,
#             'url': request.application_url + '/login',
#             'came_from': came_from,
#             'form': form,
#     }
#
#
# @view_config(route_name='logout', renderer='webapp:templates/logout.mako')
# def logout(request):
#     headers = forget(request)
#     return HTTPFound(location=request.route_url('index'),
#                      headers=headers)
#
#
# @view_config(route_name='registration', renderer='webapp:templates/registration.mako')
# def register(request):
#     try:
#         form = RegistrationForm(request.POST)
#         if request.method == 'POST' and form.validate():
#             new_user = Users()
#             new_user.name = form.username.data
#             new_user.mail = form.email.data
#             new_user.sex = form.sex.data
#             _hash = hashlib.sha224('{}'.format(time.time()).encode('utf-8')).hexdigest()
#             code = str(request.application_url + '/activate/{}'.format(_hash))
#             new_user.activate_code = code
#             try:
#                 send_mail(form.email.data, 'bundle', code)
#             except:
#                 pass
#             if form.password.data.encode('utf8') == form.confirm_password.data.encode('utf8'):
#                 new_user.set_password(form.password.data.encode('utf8'))
#             else:
#                 return {'message': 'False'}
#             DBSession.add(new_user)
#             return HTTPFound(location=request.route_url('verify'))
#         return {'form': form}
#     except DBAPIError:
#         return {'message': 'False'}


@view_config(route_name='verify', renderer='webapp:templates/verify.mako')
def verify(request):
    code = request.matchdict['code']
    response = Response()
    response.set_cookie('info', value=code, max_age=86400)
    return HTTPFound(location=request.route_url('index'), headers=response.headers)


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
    return {'message': 'about'}


@view_config(route_name='pay', renderer='webapp:templates/pay.mako')
def pay_methods(request):
    try:
        form = PaymentForm(request.POST)
        if request.method == 'POST':
            amount = request.POST['amount']
            content = request.POST['content']
            charity = request.POST['charity']
            email = request.POST['email']
            credit_card = form.card.data
            sum_content = float(amount) * float(content) / 100
            sum_charity = float(amount) * float(charity) / 100
            codec = {
                    'email': email,
                    'card': credit_card,
                    'charity': float(sum_charity),
                    'content': float(sum_content),
                    'amount': float(amount)
                }
            res = itsden_signat.dumps(codec)
            if float(form.amount.data) >= 2.0:
                bundle = DBSession.query(Bundle).filter(Bundle.date_start<=datetime.datetime.utcnow(),
                                                        Bundle.date_end>=datetime.datetime.utcnow()).first()
                if bundle is not None and (sum_charity+sum_content==float(amount)):
                    try:
                        code = request.application_url+'/verify/{}'.format(res.decode())
                        send_mail(email, 'you content', code)
                        print(code)
                        new_order = Orders(sum_charity=sum_charity, sum_content=sum_content, mail=email, bundle_id=bundle.id)
                        DBSession.add(new_order)
                        if DBSession.query(Users).filter_by(mail=email).first() is None:
                            new_user = Users()
                            new_user.mail = email
                            DBSession.add(new_user)
                        return HTTPFound(location="/")
                    except:
                        return {'message': 'check you email sender addres'}
                else:
                    return {'message': 'Bundle is not exist or sum content + sum charity != amount'}
            else:
                return {'message': 'Enter sum >= 2'}
    except DBAPIError:
        return HTTPFound(location="/")


@view_config(route_name='b_content', renderer='webapp:templates/bonus.mako')
def bonus_content(request):
    try:
        # if request.unauthenticated_userid is not None:
        dict_itsden = itsden_signat.loads(request.cookies['info'])
        order = DBSession.query(Orders).filter_by(mail=dict_itsden['email']).first()
        _sum = DBSession.query(func.sum(Orders.sum_charity+Orders.sum_content)).filter(Orders.mail==dict_itsden['email'])
        if order is not None:
            get_content_by_id = DBSession.query(Content).filter(Content.id==request.matchdict['id'],Content.tier<=_sum[0][0]).first()
            if get_content_by_id is not None:
                return {'image': '../'+get_content_by_id.image,
                        'title': get_content_by_id.title,
                        'description': get_content_by_id.description,
                        'link': get_content_by_id.link,
                        'manufacture': get_content_by_id.manufacture}
            else:
                return preview(request)
        else:
            return preview(request)
        # else:
        #     return preview(request)
    except KeyError:
        return HTTPFound(location='/')