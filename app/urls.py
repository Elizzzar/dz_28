from django.urls import path
from .views import Sign_Up, Log_out, Login, success

urlpatterns = [
    path('', Login.as_view(), name='login'),
    path('logout/', Log_out.as_view(), name='logout'),
    path('success/', success, name='success'),
    path('sign_up', Sign_Up.as_view(), name='sign_up'),
]