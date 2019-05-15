from django.conf.urls import url
# from django.urls import path
from . import testdb
from . import search
from . import search2
from django.contrib import admin

from . import view

urlpatterns = [
    # url(r'^$', view.hello),
    # path('hello/', view.hello),
    url(r'^testdb$', testdb.testdb),
    url(r'^search-form$', search.search_form),
    url(r'^search$', search.search),
    url(r'^search-post$', search2.search_post),
    url(r'^admin/', admin.site.urls)
]