from django.conf.urls import url

from .views import LoginGatewayView

urlpatterns = [
    url(r'^$', LoginGatewayView.as_view(), name='social_login'),
]
