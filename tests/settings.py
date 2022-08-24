SECRET_KEY = 'can you keep a secret?'

DEBUG = True

USE_TZ = True

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

ROOT_URLCONF = 'mozilla_django_oidc.urls'

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',

    'mozilla_django_oidc',
]

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

MIDDLEWARE = []

OIDC_USERNAME_ALGO = None

# Multitenant configuration example

OIDC_RP_CLIENT_ID = {
    'onelogin' : {
        "oidc_client_key" : { 
            'en': '09c768b0-f148-013a-731f-0a854e344251213232',
            'de': '9d8f6460-f92e-013a-a22a-029c359c6e97213232'
        }
    }
}

OIDC_RP_CLIENT_SECRET = {
    'onelogin' : {
        "oidc_client_key" : { 
            'en': '0a4e3418dccaf77a6957f83312865130811069de958fd3a4d04dd744b9351ee6123123',
            'de': '6629cdc1143838ac959b5d0c62151bbb75d91f4478e99f430bad3245c0b34030asdasdasd'
        }
    }
}

OIDC_OP_AUTHORIZATION_ENDPOINT = {
    'onelogin' : {
        "oidc_client_key" : "https://%s.onelogin.com/oidc/2/auth"
    }
}

OIDC_OP_TOKEN_ENDPOINT = {
    'onelogin' : {
        "oidc_client_key" : "https://%s.onelogin.com/oidc/2/auth"
    }
}

OIDC_OP_USER_ENDPOINT = {
    'onelogin' : {
        "oidc_client_key" : "https://%s.onelogin.com/oidc/2/auth"
    }
}

OIDC_RP_SIGN_ALGO = {
    'onelogin' : "RS256"
}

OIDC_OP_JWKS_ENDPOINT = {
    'onelogin' : "https://contentlab-dev.onelogin.com/oidc/2/certs"
}


