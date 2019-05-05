from django.conf.urls import url
from django.urls import path

from . import view

urlpatterns = [
    # url(r'^$', view.hello),
    path('hello/', view.hello)
]