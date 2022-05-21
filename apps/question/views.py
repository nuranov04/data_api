from rest_framework import viewsets, mixins

from apps.question.serializers import (
    QuestionSerializer,
    QuestionDetailSerializer,
    AnswerSerializer,
    SelectSerializer,
    SelectAnswerSerializer
)
from apps.question.models import Answer, Select, Question, SelectAnswer


class QuestionListApiView(viewsets.GenericViewSet,
                          mixins.ListModelMixin,
                          mixins.CreateModelMixin):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetailApiView(viewsets.GenericViewSet,
                            mixins.DestroyModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.RetrieveModelMixin
                            ):
    queryset = Question.objects.all()
    serializer_class = QuestionDetailSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class SelectViewSet(viewsets.ModelViewSet):
    queryset = Select.objects.all()
    serializer_class = SelectSerializer


class SelectAnswerViewSet(viewsets.ModelViewSet):
    queryset = SelectAnswer.objects.all()
    serializer_class = SelectAnswerSerializer

