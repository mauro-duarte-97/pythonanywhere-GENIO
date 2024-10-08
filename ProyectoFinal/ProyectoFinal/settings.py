"""
Django settings for ProyectoFinal project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
# from dotenv import load_dotenv # type: ignore

# Ruta del archivo .env
# env_path = Path('.') / '.env'
# load_dotenv(dotenv_path=env_path)


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/


ALLOWED_HOSTS =  [] #['MauroDuarte97.pythonanywhere.com']

LOCAL_APPS = [
    'apps.auth_user',
    'apps.custom_user',
    'apps.alumno',
    'apps.carrera',
    'apps.cursada',
    'apps.institucion',
    'apps.materia',
    'apps.opinion',
    'apps.profesor',
    'apps.feedback',
]

# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'allauth',
    'allauth.account',
]
    # 'django.contrib.sites','allauth.socialaccount','allauth.socialaccount.providers.google',

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]
#Verificación de usuario por DNI  --> 'auth_user.middleware.VerificationMiddleware'

ROOT_URLCONF = 'ProyectoFinal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ProyectoFinal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us' #es-ar

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Configuración para archivos de medios (imágenes de perfil, archivos subidos por los usuarios, etc.)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#AGREGADO MIO
AUTH_USER_MODEL = "custom_user.CustomUser"
LOGIN_REDIRECT_URL = "/userHome/"
LOGOUT_REDIRECT_URL = "/auth/login"
LOGIN_URL = '/auth/login'


# Uso de las variables de entorno
DEBUG =  os.getenv('DEBUG') == 'False' #os.getenv('DEBUG') == 'True'
SECRET_KEY = os.getenv('SECRET_KEY') # 'django-insecure-(-acc@a&^9pe#-7v-^b1ii3evm!0sw&f2j*wz(7@c2)j5qewr$' 
DATABASE_URL = os.getenv('DATABASE_URL')
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
DJANGO_GOOGLE_OAUTH2_CLIENT_ID = os.getenv('DJANGO_GOOGLE_OAUTH2_CLIENT_ID')
DJANGO_GOOGLE_OAUTH2_CLIENT_SECRET = os.getenv('DJANGO_GOOGLE_OAUTH2_CLIENT_SECRET')
DJANGO_GOOGLE_OAUTH2_PROJECT_ID = os.getenv('DJANGO_GOOGLE_OAUTH2_PROJECT_ID')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

# Si estás usando DATABASE_URL, también necesitas dj-database-url
# import dj_database_url # type: ignore
# DATABASES = {
#     'default': dj_database_url.config(default=DATABASE_URL)
# }

####### Configuración para enviar correos electrónicos #######

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

SITE_ID = 1

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)
