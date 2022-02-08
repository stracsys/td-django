from polls.views import *

from django.urls import path

urlpatterns = [
    path(
        '',
        index,
        name='home'
    ),
    path(
        'update/<int:pk>/',
        update_person,
        name='update'
    ),
    path(
        'add',
        add,
        name='add'
    ),
]
