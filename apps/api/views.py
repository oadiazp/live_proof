from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Profile
from .serializers import ProfileSerializer


class ProfileView(APIView):
    def get(self, request, *args, **kwargs):
        profile = Profile.objects.filter(
            user__username=self.request.user.username
        ).first()

        return Response(
            data=ProfileSerializer(profile).data
        )
