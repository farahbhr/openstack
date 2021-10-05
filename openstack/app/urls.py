from django.urls import path, re_path
from app import views
from .views import multitier_view
from .views import twotier_view
from .views import database_view
from .views import rules_view
from django.conf.urls import url

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    url(r'^3tier',multitier_view, name='3tier'),
    url(r'^2tier',twotier_view, name='2tier'),
    url(r'^index',views.healthcheck_view, name='index'),
    url(r'^compute',database_view, name='database'),
    url(r'^storage',views.pages, name='pages'),
    url(r'^networking',views.pages, name='pages'),
    url(r'^security',rules_view, name='security'),

]
