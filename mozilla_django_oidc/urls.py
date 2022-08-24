from django.urls import path
from django.utils.module_loading import import_string

from mozilla_django_oidc import views
from mozilla_django_oidc.utils import import_from_settings

DEFAULT_CALLBACK_CLASS = 'mozilla_django_oidc.views.OIDCAuthenticationCallbackView'
CALLBACK_CLASS_PATH = import_from_settings('OIDC_CALLBACK_CLASS', DEFAULT_CALLBACK_CLASS)

OIDCCallbackClass = import_string(CALLBACK_CLASS_PATH)


DEFAULT_AUTHENTICATE_CLASS = 'mozilla_django_oidc.views.OIDCAuthenticationRequestView'
AUTHENTICATE_CLASS_PATH = import_from_settings(
    'OIDC_AUTHENTICATE_CLASS', DEFAULT_AUTHENTICATE_CLASS
)

OIDCAuthenticateClass = import_string(AUTHENTICATE_CLASS_PATH)

urlpatterns = [
    path('callback/', OIDCCallbackClass.as_view(), name='oidc_authentication_callback'),
    path('authenticate/', OIDCAuthenticateClass.as_view(), name='oidc_authentication_init'),
    path('callback/(?P<oidc_client_key>.+)/$', OIDCCallbackClass.as_view(),
        name='oidc_authentication_callback_multiple_clients'),
    path('authenticate/(?P<oidc_client_key>.+)/$', OIDCAuthenticateClass.as_view(),
        name='oidc_authentication_init_multiple_clients'),
    path('logout/', views.OIDCLogoutView.as_view(), name='oidc_logout'),
]
