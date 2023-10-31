from django.urls import path
from .views import geeks_view, geeks_modelform

urlpatterns = [
    path('', geeks_view, name='geeks_view2'),
    path('add/', geeks_modelform, name='geeks_form'),
]
