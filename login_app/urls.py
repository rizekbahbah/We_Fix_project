from django.urls import path 
from . import views
urlpatterns = [
    path('log-in' , views.log_in )
]
