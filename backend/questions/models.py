from django.db import models

from core.models import TimestampedModel
from core.utils import cut_string


class Question(TimestampedModel):
    '''Сущность `Вопрос`.'''

    id_question = models.IntegerField('идентификатор вопроса')
    question = models.TextField('текст вопроса')
    answer = models.TextField('текст ответа')
    created_question_at = models.DateTimeField('дата создания вопроса')

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'
        get_latest_by = 'pk'

    def __str__(self) -> str:
        return cut_string(f'Вопрос №{self.id_question}')
