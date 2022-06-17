# DevSearch
VirtualOfficeRoom


[WhiteNoise](http://whitenoise.evans.io/en/stable/)
Installation

```pip install whitenoise```

Edit your settings.py file and add WhiteNoise to the MIDDLEWARE list, above all other middleware apart from Django’s SecurityMiddleware:
```
MIDDLEWARE = [
    # ...
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # ...
]
```
