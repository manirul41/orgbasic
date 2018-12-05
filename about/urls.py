from django.urls import path

from about import views

urlpatterns = [
    path('', views.AboutView.as_view(), name='about'),
    path('members/', views.ShowAllMembers.as_view(), name='members'),
    path('member-details/', views.ShowMemberDetails.as_view(), name='member-details'),
]
