from django.urls import path
from .import views

app_name ='login'
urlpatterns = [
    path('',views.index,name="index"),
    path('signup/',views.signup,name="signup"),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name="logout"),
    path('fail/',views.fail,name="fail"),
    path('success/', views.success,name="success"),
    path('loginsuccess/', views.loginsuccess,name="loginsuccess"),
    path('change_pw/',views.change_pw,name="change_pw"),
]