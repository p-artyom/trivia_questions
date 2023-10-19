from rest_framework import serializers

from questions.models import Question


class GetQuestionSerializer(serializers.Serializer):
    questions_num = serializers.IntegerField()

    def validate_questions_num(self, value: int) -> int:
        if value <= 0:
            raise serializers.ValidationError(
                'Введите положительное число!',
            )
        return value


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'id',
            'id_question',
            'question',
            'answer',
            'created_question_at',
            'created',
            'modified',
        )
