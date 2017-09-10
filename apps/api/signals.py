from django.dispatch import receiver

from allauth.account.signals import user_signed_up


@receiver(user_signed_up)
def create_profile(request, user, **kwargs):
    from apps.api.models import Profile

    Profile.objects.create(user=user)
