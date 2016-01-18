from pyramid.response import Response
from pyramid.renderers import get_renderer
from pyramid.httpexceptions import HTTPFound
from .form import RegistrationForm, LoginForm, PaymentForm
from .models import Users, Content, Orders
from sqlalchemy.exc import DBAPIError
from passlib.apps import custom_app_context as check_password
from .models import (
    DBSession,

    )

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


def users_check(func):
    def wrapper(user_name):
        if user_name is not None:
            query = DBSession.query(Users).filter(Users.name == user_name).first()
            if query.is_active:
                func()
                return True


@view_config(route_name='content', renderer='templates/content.pt')
def content(request):
    check_user = None
    if request.unauthenticated_userid is not None:
        user = DBSession.query(Users).filter_by(name=request.unauthenticated_userid).first()
        order = DBSession.query(Orders).filter_by(mail=user.mail).first()
        if order.id is not None:
            check_user = DBSession.query(Content).filter_by(bundle_id=order.bundle_id).first()
            return {'title': check_user.title,
                    'description': check_user.description,
                    'link': check_user.link,
                    'image': '../'+check_user.image,
                    }
        else:
            return {'title': check_user.title,
                    'description': check_user.description,
                    'link': check_user.link,
                    'image': '../'+check_user.image,
                    }
    # try:
    #     query = DBSession.query(Content).filter_by(id=request.matchdict['id']).first()
    # except:
    #     return HTTPFound(location='/')
    # return Response(content_type='text/plain', status_int=500)


@view_config(route_name='preview', renderer='templates/preview.pt')
def preview(request):
    try:

        if request.unauthenticated_userid is None:
            return {
                'form': PaymentForm(request.POST),
                'login_status': 'login',
                'link': '/login',
                'content': content
            }
    except DBAPIError:
        return Response(content_type='text/plain', status_int=500)


@view_config(route_name='index', renderer='templates/index.pt')
def index(request):
    try:
        form = PaymentForm(request.POST)
        # mailer = request.registry['mailer']
        if request.unauthenticated_userid is not None:
            return {'form': form,
                    'login_status': 'Welcome, '+request.unauthenticated_userid,
                    'link': '/logout',
                    'content': content(request)
                    }
        elif request.unauthenticated_userid is None:
            return preview(request)
    except DBAPIError:
        return Response(content_type='text/plain', status_int=500)


@view_config(route_name='login', renderer='templates/login.pt')
@forbidden_view_config(renderer='templates/login.pt')
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
        db_query = DBSession.query(Users).filter(Users.name == login).first()
        if db_query.name == login and check_password.verify(password.encode('utf-8'), db_query.password):
            headers = remember(request, login)
            return HTTPFound(location=request.route_url('index'),
                             headers=headers)
        message = 'Failed login'

    return dict(
            message=message,
            url=request.application_url + '/login',
            came_from=came_from,
            form=form,
    )


@view_config(route_name='logout', renderer='templates/logout.pt')
def logout(request):
    headers = forget(request)
    return HTTPFound(location = request.route_url('index'),
                     headers = headers)


@view_config(route_name='registration', renderer='templates/registration.pt')
def register(request):
    form = RegistrationForm(request.POST)
    if request.method == 'POST' and form.validate():
        new_user = Users()
        new_user.name = form.username.data
        new_user.mail = form.email.data
        new_user.sex = form.sex.data
        _hash = hashlib.sha224('{}'.format(time.time()).encode('utf-8')).hexdigest()
        new_user.activate_code = str(request.application_url + '/activate/{}'.format(_hash))
        if form.password.data.encode('utf8') == form.confirm_password.data.encode('utf8'):
            new_user.set_password(form.password.data.encode('utf8'))
        else:
            return {'success': 'False'}
        DBSession.add(new_user)
        return HTTPFound(location=request.route_url('index'))
    return {'form': form}


@view_config(route_name='end_reg', renderer='templates/confirm.pt')
def end_reg(request):
    try:
        db_query = DBSession.query(Users).filter(Users.activate_code == request.url).first()
        if db_query.activate_code is not None:
            if request.url == db_query.activate_code:
                DBSession.query(Users).filter_by(id=db_query.id).update({'is_active': True})
                return HTTPFound(location=request.route_url('index'))
        return HTTPFound(location=request.route_url('index'))
    except Exception as e:
        print(e)
    return {'message': 'You account is activate!'}


@view_config(route_name='bundles', renderer='templates/bundles.pt')
def bundles(request):
    form = PaymentForm(request.POST)
    # if request.method == 'POST' and form.validate():
    #     amount = form.amount.data
    #     email = form.email.data
    return {'form': form, 'message': 'test'}