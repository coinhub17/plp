from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name='realtekrealty'

urlpatterns = [
    path('',views.index, name='index'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
    path('hse',views.hse, name='hse'),
    path('vhse', views.vhse, name='vhse'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('dashboard',views.dashboard,name='dashboard'),
    path("search",views.search,name="search")
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)