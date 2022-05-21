from rest_framework.routers import DefaultRouter

from apps.question.views import (QuestionListApiView,
                                 QuestionDetailApiView,
                                 AnswerViewSet,
                                 SelectViewSet,
                                 SelectAnswerViewSet,
                                 )

router = DefaultRouter()
router.register(
    prefix='question',
    viewset=QuestionListApiView
)
router.register(
    prefix='question',
    viewset=QuestionDetailApiView
)
router.register(
    prefix='answer',
    viewset=AnswerViewSet
)
router.register(
    prefix='select',
    viewset=SelectViewSet
)
router.register(
    prefix='select_answer',
    viewset=SelectAnswerViewSet
)

urlpatterns = router.urls
