from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Profile, Insurance
from .serializers import ProfileSerializer, InsuranceSerializer


class ProfileView(APIView):
    def get(self, request, *args, **kwargs):
        profile = Profile.objects.filter(
            user__username=self.request.user.username
        ).first()

        return Response(
            data=ProfileSerializer(profile).data
        )


class InsuranceViewSet(ModelViewSet):
    serializer_class = InsuranceSerializer

    def get_queryset(self):
        return Insurance.objects.filter(
            profile__user__username=self.request.user.username
        )
