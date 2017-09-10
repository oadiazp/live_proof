from django.conf.urls import url

from .views import LoginGatewayView, ProfileView

urlpatterns = [
    url(r'^$', LoginGatewayView.as_view(), name='social_login'),
    url(r'^accounts/profile', ProfileView.as_view(), name='profile'),
]
