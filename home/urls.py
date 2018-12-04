from django.contrib.auth.decorators import login_required
from django.urls import path

from home import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
]
