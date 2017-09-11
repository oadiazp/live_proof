import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


class TestProfile:
    def test_get_social_networks_connected_to_this_profile(self):
        user = mixer.blend('auth.User')
        profile = mixer.blend('api.Profile', user=user)

        for provider in ['google', 'facebook']:
            mixer.blend(
                'socialaccount.SocialAccount',
                user=user,
                provider=provider
            )

        associated_social_network_accounts = (
            profile.associated_social_network_accounts
        )

        assert len(associated_social_network_accounts) == 2
        assert associated_social_network_accounts.filter(
            provider__in=['google', 'facebook']
        )
