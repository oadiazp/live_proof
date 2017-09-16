from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer, Serializer

from .models import Profile, Insurance, Destination


class SocialNetworkSerializer(Serializer):
    name = serializers.CharField(source='provider')


class InsuranceSerializer(ModelSerializer):
    created_humanized = SerializerMethodField()

    class Meta:
        model = Insurance
        fields = ('name', 'created_humanized', 'enabled', 'id', 'profile')

    def get_created_humanized(self, obj):
        return naturaltime(obj.created)


class ProfileSerializer(ModelSerializer):
    first_name = SerializerMethodField()
    last_name = SerializerMethodField()
    social_networks = SerializerMethodField()
    insurances = SerializerMethodField()

    class Meta:
        model = Profile
        fields = (
            'first_name',
            'last_name',
            'picture',
            'social_networks',
            'insurances',
        )

    @property
    def user(self):
        return self.instance.user

    def get_first_name(self, obj):
        return self.user.first_name

    def get_last_name(self, obj):
        return self.user.last_name

    def get_social_networks(self, obj):
        return SocialNetworkSerializer(
            obj.associated_social_network_accounts,
            many=True
        ).data

    def get_insurances(self, obj):
        return InsuranceSerializer(
            Insurance.objects.filter(profile=obj),
            many=True
        ).data


class DestinationSerializer(ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'
