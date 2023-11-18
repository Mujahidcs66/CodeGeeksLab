from django.urls import path
from .views import index, remove

urlpatterns = [
    path('', index, name='todo'),
    path('delete/<str:item_id>', remove, name='delete'),
]
