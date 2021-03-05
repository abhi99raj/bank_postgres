from django.urls import path, include
from bank_details.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('crud', views.BranchesViewSet, basename='branches')

urlpatterns = [
    path('', include(router.urls))
]
