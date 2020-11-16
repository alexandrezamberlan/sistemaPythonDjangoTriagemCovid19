from __future__ import unicode_literals
from django.conf.urls import url
from .views import HomeView, AboutView

urlpatterns = [
   url(r'^home$', HomeView.as_view(), name='home'),
   url(r'^about$', AboutView.as_view(), name='about'),
]