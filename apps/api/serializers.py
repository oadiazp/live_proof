from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from apps.api.models import Profile


class ProfileSerializer(ModelSerializer):
    first_name = SerializerMethodField()
    last_name = SerializerMethodField()
    social_networks = SerializerMethodField()

    class Meta:
        model = Profile
        fields = (
            'first_name',
            'last_name',
            'picture',
            'social_networks',
        )

    @property
    def user(self):
        return self.instance.user

    def get_first_name(self, obj):
        return self.user.first_name

    def get_last_name(self, obj):
        return self.user.last_name

    def get_social_networks(self, obj):
        return []
