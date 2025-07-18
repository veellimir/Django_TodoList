from rest_framework.routers import DefaultRouter

from settings import SuffixRouter
from .views import TaskViewSet, CategoryViewSet

router = DefaultRouter()

router.register(SuffixRouter.TASKS, TaskViewSet, basename='task')
router.register(SuffixRouter.CATEGORIES, CategoryViewSet)

urlpatterns = router.urls
