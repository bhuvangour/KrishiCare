from django.urls import path
from . import views

urlpatterns = [
    path('consult', views.chatbot_view, name='consult'), 
]
