from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_form_view, name='user_form'),
    path('index.html', views.user_form_view, name='user_form'),
    path('delete-applicant/<int:id>/', views.delete_applicant, name='delete_applicant'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-logout/', views.admin_logout, name='admin_logout'),
]