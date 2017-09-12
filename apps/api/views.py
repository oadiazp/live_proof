from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Profile, Insurance, Destination
from .serializers import (
    ProfileSerializer,
    InsuranceSerializer,
    DestinationSerializer,
)


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


class DestinationViewSet(ModelViewSet):
    serializer_class = DestinationSerializer

    def get_queryset(self):
        return Destination.objects.filter(
            insurance__id=self.kwargs['pk']
        )
