from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('write/', views.write_message, name='write'),
    path('get_all/', views.get_all_messages_for_receiver, name='get_all_reciver'),
    path('get_unread/', views.get_unread_messages_for_receiver, name='get_unread_reciver'),    
    path('read/', views.read_message, name='read'),
    path('delete/', views.delete_message, name='delete'),
]

