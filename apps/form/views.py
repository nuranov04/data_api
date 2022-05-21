from rest_framework import viewsets, mixins, permissions

from apps.form.models import Form
from apps.form.serializers import FormListSerializer, FormDetailSerializer


class FormListApiView(viewsets.GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin):
    queryset = Form.objects.all()
    serializer_class = FormListSerializer


class FormDetailApiView(viewsets.GenericViewSet,
                        mixins.DestroyModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.RetrieveModelMixin
                        ):
    queryset = Form.objects.all()
    serializer_class = FormDetailSerializer
