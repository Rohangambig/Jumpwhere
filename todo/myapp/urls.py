from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login_page,name='login'),
    path('',views.signup_page,name='signup'),
    path('home/',views.homePage,name = 'homepage'),
    path('register/',views.Register_user,name= "register"),
    path('login_user/',views.login_user,name='login_user'),
    path('get_user/',views.get_user_data,name='get_user')
]