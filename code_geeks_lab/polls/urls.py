from django.urls import path
from .views import detail, index, results, vote

urlpatterns = [
    path('', index, name='polls'),
    path('<int:question_id>/', detail, name ='detail'),
    path('<int:question_id>/results/', results, name ='results'),
    path('<int:question_id>/vote/', vote, name ='vote'),
]
