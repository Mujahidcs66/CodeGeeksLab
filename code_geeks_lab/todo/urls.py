from django.urls import path
from .views import index, remove

urlpatterns = [
    path('', index, name='index'),
    path('delete/<str:item_id>', remove, name='delete'),
]
