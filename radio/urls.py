from django.urls import path
from . import views

app_name='radio'

urlpatterns = [    path('my_url/', views.my_view, name='my_view'),]
