from django.urls import path
from . import views

app_name = 'team'
urlpatterns = [
    path('', views.team_members, name='team_members'),
    path('add/', views.add_team_member, name='add_team_member'),
    path('<int:pk>/', views.team_member_detail, name='team_member_detail'),
    path('<int:pk>/edit/', views.edit_team_member, name='edit_team_member'),
    path('<int:pk>/delete/', views.delete_team_member, name='delete_team_member'),
]
