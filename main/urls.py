



from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jikken',views.jikken, name='jikken'),
    path('signup',views.jikken, name='signup'),
    path('mylogin',views.mylogin, name='mylogin'),
    path('form_login',views.form_login, name='form_login'),
    path('register',views.register, name='register'),
    path('panel',views.panel,name='panel')
]
