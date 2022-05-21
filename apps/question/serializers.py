from rest_framework import serializers

from apps.question.models import Question, Answer, Select, SelectAnswer


class SelectAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelectAnswer
        fields = "__all__"


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"


class SelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Select
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'id',
            'question',
            'form',
            'type',

        )


class QuestionDetailSerializer(serializers.ModelSerializer):
    select = SelectSerializer(many=True, read_only=True)
    answer = AnswerSerializer(many=True, read_only=True)
    question_select_answers = SelectAnswerSerializer(read_only=True, many=True)

    class Meta:
        model = Question
        fields = (
            'id',
            'form',
            'question',
            'type',
            'select',
            'answer',
            'question_select_answers',
        )
