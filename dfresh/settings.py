"""
Django settings for dfresh project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import sys, os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')nbc^i+ldfid72z$ree^zyn-k&)=^_^4(=ap1ee+4ueixa17+7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition
# 增加了注册应用
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tinymce',
    'haystack',
    'apps.user.apps.UserConfig',
    'apps.cart.apps.CartConfig',
    'apps.goods.apps.GoodsConfig',
    'apps.order.apps.OrderConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dfresh.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'dfresh.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
# 修改自用的数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'xxx',
        'USER': 'xxx',
        'PASSWORD': 'xxx',
        'HOST': 'xxx',
        'PORT': 3306,
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# -----------------------------------------------------------------------------
# 搜索框架haystack配置
HAYSTACK_CONNECTIONS = {
    'default': {
        # use whoosh engine
        # 'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'ENGINE': 'haystack.backends.whoosh_cn_backend.WhooshEngine',
        # Index file path
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    }
}


# Celery相关配置
# 配置redis作为broker消息代理
broker_url = 'redis://ip:port/database_id'
result_backend = 'redis://ip:port/database_id'
result_backend_transport_options = {'visibility_timeout': 18000}  # 5 hours
timezone = 'Asia/Shanghai'
# 更多参数：https://docs.celeryproject.org/en/stable/userguide/configuration.html


# 配置cache
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://ip:port/database_id",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}


# 配置session
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"


# django自带模块设置
# 系统默认的用户验证类为：’auth.User’
# 修改用户验证类为自定义：‘user.User’
AUTH_USER_MODEL = 'user.User'
# 设置authenticate不关联is_activate
AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.AllowAllUsersModelBackend']
# 配置默认的登录URL地址
LOGIN_URL = '/user/login'


# fastdfs设置
FDFS_CLIENT_CONF = './utils/client.conf'
FDFS_STORAGE_URL = 'http://ip:port'  # nginx服务器
DEFAULT_FILE_STORAGE = 'utils.fdfs_storage.FdfsStorage'


# tinymce富文本编辑器参数
TINYMCE_DEFAULT_CONFIG = {
    'theme': 'silver',
    'width': 600,
    'height': 400,
}


# 126 email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.126.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'your_email_address'  # 发送邮件的邮箱
EMAIL_HOST_PASSWORD = 'token'  # 邮箱授权码
# EMAIL_USE_TLS = True  # 与SMTP服务器通信时，是否启动TLS链接(安全链接)
EMAIL_FROM = '天天生鲜<your_email_address>'  # EMAIL_FROM 和 EMAIL_HOST_USER必须一样


# 支付宝沙箱APP_ID
ALIPAY_APP_ID = 'your_alipay_app_id'
# 支付宝网站回调url地址
ALIPAY_APP_NOTIFY_URL = None
# 支付宝同步return_url地址
ALIPAY_APP_RETURN_URL = 'http://127.0.0.1:8000/order/check'
# 网站私钥文件路径
APP_PRIVATE_KEY = os.path.join(BASE_DIR, 'utils/app_private_key.pem')
# 支付宝公钥文件路径
ALIPAY_PUBLIC_KEY = os.path.join(BASE_DIR, 'utils/alipay_public_key.pem')
# 支付宝支付的开发模式
ALIPAY_DEBUG = True
# 支付宝沙箱支付网关地址
ALIPAY_GATEWAY_URL = 'https://openapi.alipaydev.com/gateway.do?'


try:
    from local_settings import *
except ImportError:
    pass


# 创建local_settings.py，复制以下内容修改
# # STATIC_ROOT = '/home/steven/static'
#
# # celery生成静态Index地址
# STATIC_INDEX_PATH = '/www/wwwroot/index.html'
#
#
# # 修改自用的数据库
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'dfresh',
#         'USER': 'root',
#         'PASSWORD': 'xxx',
#         'HOST': 'localhost',
#         'PORT': 3306,
#     }
# }
#
#
# # Celery相关配置
# # 配置redis作为
# CELERY_BROKER_URL = 'redis://localhost:6379/3'
# CELERY_RESULT_BACKEND = 'redis://localhost:6379/3'
# CELERY_TIMEZONE = 'Asia/Shanghai'
# # 更多参数：https://docs.celeryproject.org/en/stable/userguide/configuration.html
#
#
# # 配置cache
# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://localhost:6379/1",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         }
#     }
# }
#
#
# # fastdfs设置
# FDFS_CLIENT_CONF = './utils/client.conf'
# FDFS_STORAGE_URL = 'http://xxxx.xxxx.xxxx.xxxx/'  # locakhost或另一台nginx服务器
# DEFAULT_FILE_STORAGE = 'utils.fdfs_storage.FdfsStorage'
#
#
# # 126 email
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.126.com'
# EMAIL_PORT = 25  # 465
# EMAIL_HOST_USER = 'xxxxxxx@126.com'  # 发送邮件的邮箱
# EMAIL_HOST_PASSWORD = 'xxxxxxxxx'  # 邮箱授权码
# # EMAIL_USE_TLS = True  # 与SMTP服务器通信时，是否启动TLS链接(安全链接)
# # EMAIL_USE_SSL = True  # 用465端口时开启
# EMAIL_FROM = '天天生鲜<xxxxxxx@126.com>'  # EMAIL_FROM 和 EMAIL_HOST_USER必须一样
#
#
#
# # 支付宝沙箱APP_ID
# ALIPAY_APP_ID = 'xxxxxxxxxxxx'
# # 支付宝网站回调url地址
# ALIPAY_APP_NOTIFY_URL = None
# # 支付宝同步return_url地址
# ALIPAY_APP_RETURN_URL = 'http://localhost:8000/order/check'


