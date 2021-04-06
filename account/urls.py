from django.urls import path
from . import views
app_name = 'account'
urlpatterns = [
    path('home/',views.Home.as_view(), name='home'),
    path('register/', views.registerview.as_view(), name = 'register'),
    path('login/', views.Loginview.as_view(), name = 'login'),
    path('logout/', views.Logoutview.as_view(), name = 'logout'),
    path('details/', views.Detailsview.as_view(), name= 'details1'),
    path('approve/<int:pk>/', views.approve, name= 'approve'),
    path('unapprove/<int:pk>/', views.unapprove, name= 'unapprove'),
    path('delete/<int:pk>/', views.delete, name= 'delete'),
]