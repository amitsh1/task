from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('write/', views.write_message, name='write'),
    path('get_all/<str:receiver>', views.get_all_messages_for_receiver, name='get_all_reciver'),
    path('get_unread/<str:receiver>', views.get_unread_messages_for_receiver, name='get_unread_reciver'),
    path('read/<str:message_id>', views.read_message, name='read'),
    path('delete/<str:message_id>', views.delete_message, name='delete'),
]

