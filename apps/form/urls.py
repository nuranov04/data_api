from rest_framework.routers import DefaultRouter

from apps.form.views import FormListApiView, FormDetailApiView


router = DefaultRouter()
router.register(
    prefix='form',
    viewset=FormListApiView
)
router.register(
    prefix='form',
    viewset=FormDetailApiView
)

urlpatterns = router.urls