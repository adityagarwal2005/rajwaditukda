from .base import *  # noqa: F401,F403

DEBUG = False

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 60 * 60 * 24 * 7  # 1 week, raise once confirmed working
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# EMAIL_BACKEND (Resend via Anymail) is inherited from base.py.

# Whitenoise serves collected static files in production. Override just the
# "staticfiles" backend here rather than setting the legacy STATICFILES_STORAGE
# setting, which Django 5 forbids combining with the STORAGES dict in base.py.
STORAGES["staticfiles"]["BACKEND"] = "apps.core.storage.LenientManifestStaticFilesStorage"
