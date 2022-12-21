from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='index'),
   # path('member_login',views.member_login,name='member_login')
]
