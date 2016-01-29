from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from pyramid_mailer.mailer import Mailer
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from .security import groupfinder

from .models import (
    DBSession,
    Base,
    )


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    authn_policy = AuthTktAuthenticationPolicy('sosecret', callback=groupfinder, hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()
    config = Configurator(settings=settings, root_factory='webapp.models.RootFactory')
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)
    config.registry['mailer'] = Mailer.from_settings(settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('index', '/')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_route('registration', '/registration')
    # config.add_route('end_reg', '/activate/{a_code}')
    config.add_route('verify', '/verify/{code}')
    # config.add_route('confirm', '/confirm')
    config.add_route('content', '/content/{id}')
    config.add_route('about', '/about')
    config.add_route('pay', '/pay')
    config.add_route('preview', '/preview')
    config.add_route('bundle_preview', '/bundle_preview')
    config.add_route('b_content', '/bonus/{id}')
    config.add_route('bundle', '/bundle/{id}')
    config.add_route('account', '/account/{parameters}')
    config.scan()

    return config.make_wsgi_app()
