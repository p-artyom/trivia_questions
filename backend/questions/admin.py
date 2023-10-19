from django.contrib import admin

from core.admin import BaseAdmin
from questions.models import Question


@admin.register(Question)
class QuestionAdmin(BaseAdmin):
    list_display = (
        'pk',
        'id_question',
        'question',
        'answer',
        'created_question_at',
        'created',
        'modified',
    )
    search_fields = ('question',)
