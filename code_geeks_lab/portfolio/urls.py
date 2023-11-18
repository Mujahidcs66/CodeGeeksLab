from django.urls import path

from .views import post_detailview, comments

urlpatterns = [
    path('<int:id>', post_detailview, name='comment'),
    path('', comments, name='comments')
]
