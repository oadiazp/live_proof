from django.conf.urls import url

from apps.api.views import ProfileView

urlpatterns = [
    url(r'profile/', ProfileView.as_view(), name='profile'),
]
