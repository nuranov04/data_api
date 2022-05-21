from rest_framework import serializers

from apps.form.models import Form
from apps.question.serializers import QuestionDetailSerializer


class FormListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = "__all__"
        read_only_fields = [
            'form_uid'
        ]


class FormDetailSerializer(serializers.ModelSerializer):
    question = QuestionDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Form
        fields = (
            'id',
            'title',
            'description',
            'create_at',
            'form_uid',
            'question',

        )
        read_only_fields = (
            'form_uid',
        )
