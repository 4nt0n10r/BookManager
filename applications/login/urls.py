from django.urls import path
from . import views as vw

urlpatterns = [
    path('', vw.IndexView.as_view(), name='index'),
    path('signin/', vw.SigninView.as_view(), name='signin'),
    path('signup/', vw.SignupView.as_view(), name='signup'),
    path('logout/', vw.LogoutView.as_view(), name='logout'),
]
