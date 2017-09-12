from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import ProfileView, InsuranceViewSet, DestinationViewSet

router = DefaultRouter()
router.register(r'insurances', InsuranceViewSet, base_name='insurances')

destination_router = DefaultRouter()
destination_router.register(
    r'destinations',
    DestinationViewSet,
    base_name='destinations'
)

urlpatterns = [
    url(r'profile/', include(router.urls)),
    url(r'profile/insurances/(?P<pk>\d+)/', include(destination_router.urls)),
    url(r'profile$', ProfileView.as_view(), name='profile'),
]
