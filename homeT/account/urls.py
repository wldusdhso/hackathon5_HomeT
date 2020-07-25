from django.urls import path
from . import views
from .forms import SigninForm

app_name='account'

urlpatterns = [ 
    path('', views.signin, name="signin"),
    path('signup/', views.signup, name='signup'),
    path("signout/", views.signout, name="signout"),
]
    