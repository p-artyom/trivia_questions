from django.urls import path

from api.views import get_questions

urlpatterns = [
    path('get_questions/', get_questions),
]
