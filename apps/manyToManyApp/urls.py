from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^view_users$', views.view_users),
    url(r'^add$', views.add),
    url(r'^view_interests$', views.view_interests)
]
