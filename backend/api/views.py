import requests
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from api.serializers import GetQuestionSerializer, QuestionSerializer
from questions.models import Question


@api_view(['POST'])
def get_questions(request: Request) -> Response:
    last_objects = get_last_object()
    request_data = GetQuestionSerializer(data=request.data)
    if not request_data.is_valid():
        return Response(
            request_data.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )
    request = send_request(request_data.data['questions_num'])
    for data in request:
        id_question = data['id']
        while Question.objects.filter(id_question=id_question).exists():
            data = send_request()
            id_question = data[0]['id']
        Question.objects.create(
            id_question=id_question,
            question=data['question'],
            answer=data['answer'],
            created_question_at=data['created_at'],
        )
    return Response(last_objects, status=status.HTTP_201_CREATED)


def send_request(questions_num: int = 1) -> Request:
    return requests.get(
        url=settings.URL,
        params={'count': questions_num},
    ).json()


def get_last_object() -> dict:
    try:
        return QuestionSerializer(Question.objects.latest()).data
    except ObjectDoesNotExist:
        return {}
