from django.urls import path
from authapp import views

urlpatterns = [
    path("", views.Home, name="Home"),
    path("signup", views.signup, name="signup"),
    path("login", views.login, name="Login"),
    path("logout", views.handleLogout, name="handleLogout"),
    path("contact", views.contact, name="contact"),
    path("join", views.enroll, name="enroll"),
    path('attendance',views.attendance,name="attendance"),
    path('profile',views.profile, name="profile"),

]
