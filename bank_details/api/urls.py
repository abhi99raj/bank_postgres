from django.urls import path, include
from bank_details.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('crud', views.BranchesViewSet, basename='branches')
router.register('crud2', views.CityViewSet, basename='cityfilter')

urlpatterns = [
    path('', include(router.urls)),
    path('search_ifsc/', views.search_ifsc),
]
