from django.urls import path
from . import views
app_name = 'teacher'

urlpatterns = [
    path("add/", views.Addview.as_view(), name='add'),
    path('classroom/',views.Classview.as_view(), name="classroom"),
    path('more/<int:pk>/',views.Dview.as_view(), name="detail"),
]