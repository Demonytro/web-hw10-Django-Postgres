from django.urls import path

from . import views

from django.contrib.auth.views import LogoutView   #LoginView,

from .forms import LoginForm
from .views import RegisterView#, LoginView

app_name = "users"

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='signup'),

    path('signin/', views.signin, name='signin'),

    # path('signin/', LoginView.as_view(
    #     template_name="users/signin.html",
    #     authentication_form=LoginForm,
    #     redirect_authenticated_user=True
    # ), name='signin'),

    # path('signin/', LoginView.as_view(), name='signin'),
    # path('signup/', views.signup, name='signup'),

    path('logout/', views.logoutuser, name='logoutuser'),
]
