from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import ProfileView, InsuranceViewSet

router = DefaultRouter()
router.register(r'insurances', InsuranceViewSet, base_name='insurances')

urlpatterns = [
    url(r'profile/', include(router.urls)),
    url(r'profile$', ProfileView.as_view(), name='profile'),
]

