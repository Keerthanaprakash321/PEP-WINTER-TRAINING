from django.urls import path
from . import views
#from .views import form_view, home_view, login_view, signup_view
urlpatterns=[
    path("polls/", views.index, name="index"),
    path("",views.index, name="user"),
    path("home/", views.home_view, name="home"),
    path("form/", views.form_view, name='form_view'),
    path("login/", views.login_view, name='login'),
    path("signup/", views.signup_view, name='signup'),
]