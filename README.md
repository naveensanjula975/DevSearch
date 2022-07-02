# DevSearch

VirtualOfficeRoom

Django [documentation](https://docs.djangoproject.com/en/4.0/)

[WhiteNoise](http://whitenoise.evans.io/en/stable/)

# Installation

`pip install whitenoise`

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
<li>Designing databases with Django
<li>
<li>Build a review and voting system
<li>User Registration and Authentication
<li>Search & Pagination
<li>Search + Pagination Hacky Fix
<li>
<li>

## Displaying messages¶

get_messages [[request]](https://docs.djangoproject.com/en/4.0/_modules/django/contrib/messages/api/#get_messages)

```
{% if messages %}
<ul class="messages">
    {% for message in messages %}
    <li{% if message.tags %} class="{{ message.tags }}"{% endif %}>{{ message }}</li>
    {% endfor %}
</ul>
{% endif %}
```

## The Paginator class

Under the hood, all methods of [pagination](https://docs.djangoproject.com/en/4.0/ref/paginator/#django.core.paginator.Paginator) use the Paginator class. It does all the heavy lifting of actually splitting a QuerySet into [Page](https://docs.djangoproject.com/en/4.0/ref/paginator/#django.core.paginator.Page) objects.

```
>>> from django.core.paginator import Paginator
>>> objects = ['john', 'paul', 'george', 'ringo']
>>> p = Paginator(objects, 2)

>>> p.count
4
>>> p.num_pages
2
```

## Sending email

Mail is sent using the SMTP host and port specified in the **EMAIL_HOST** and **EMAIL_PORT** settings. The **EMAIL_HOST_USER** and **EMAIL_HOST_PASSWORD** settings, if set, are used to authenticate to the SMTP server, and the **EMAIL_USE_TLS** and **EMAIL_USE_SSL** settings control whether a secure connection is used.

```
from django.core.mail import send_mail

send_mail(
    'Subject here',
    'Here is the message.',
    'from@example.com',
    ['to@example.com'],
    fail_silently=False,
)
```
