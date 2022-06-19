# DevSearch
VirtualOfficeRoom


Django [documentation](https://docs.djangoproject.com/en/4.0/)¶


[WhiteNoise](http://whitenoise.evans.io/en/stable/)

# Installation

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


<li>Build a Django website
<li>Hosting a website on a live server
<li>Build a review and voting system
<li>User Login, Logout and Flash Messages
<li>
<li>
<li>
<li>
