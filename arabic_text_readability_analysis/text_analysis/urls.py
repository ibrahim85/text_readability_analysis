from django.urls import path, include
from . import views
# from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', views.home_page, name="home_page"),
]