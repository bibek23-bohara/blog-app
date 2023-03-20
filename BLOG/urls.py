
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("blog_app.urls")),
    path("accounts/login/" , LoginView.as_view(), name="login"),
    path("accounts/logout/", LogoutView.as_view(), name="logout"),

]
handler404 = "blog_app.views.handler404"