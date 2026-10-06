""" URLs for User Authentication """

from django.urls import include, path
from django.views.generic.base import RedirectView

from .views import auth, login, login_form

urlpatterns = [
    # TODO move contents of urls_common here once CMS no longer has its own login
    path('', include('openedx.core.djangoapps.user_authn.urls_common')),
    path('api/', include('openedx.core.djangoapps.user_authn.api.urls')),
    path('account/finish_auth', login.finish_auth, name='finish_auth'),
    path('auth/jwks.json', auth.get_public_signing_jwks, name='get_public_signing_jwks'),
]


# Backwards compatibility with old URL structure, but serve the new views
urlpatterns += [
    path('login', login_form.login_and_registration_form,
         {'initial_mode': 'login'}, name='signin_user'),
    # FinishingX: self-service signup is disabled; send would-be registrants to the
    # request-demo page instead. Login and password reset are unaffected.
    path('register', RedirectView.as_view(url='/pages/request-demo/', permanent=False),
         name='register_user'),
    path('password_assistance', login_form.login_and_registration_form,
         {'initial_mode': 'reset'}, name='password_assistance'),
]
