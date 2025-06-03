from django.urls import path
from django.contrib.auth import views as author_views
from . import views

app_name = "users"

urlpatterns = [
    path('signup/', views.signup_view, name="signup"),
    path("login/", author_views.LoginView.as_view(template_name="user/login.html"), name="login"),
    path("logout/", author_views.LoginView.as_view(), name="logout"),

]
