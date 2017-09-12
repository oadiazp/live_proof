from allauth.socialaccount.models import SocialAccount

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel

from .choices import NamedChoices


class StringOverridedModel:
    def __str__(self):
        return self.name


class Insurance(TimeStampedModel, StringOverridedModel):
    name = models.CharField(max_length=200)
    enabled = models.BooleanField(default=False)

    profile = models.ForeignKey('Profile')

    class Meta:
        ordering = ('created',)


CHANNEL = NamedChoices((
    ('EMAIL', _('E-mail')),
))


class Destination(TimeStampedModel, StringOverridedModel):
    name = models.CharField(max_length=200)

    insurance = models.ForeignKey(Insurance)
    channel = models.CharField(
        max_length=CHANNEL.max_length,
        choices=CHANNEL
    )


class LiveProof(TimeStampedModel):
    proofed = models.BooleanField(default=False)

    insurance = models.ForeignKey(Insurance)


class Profile(TimeStampedModel):
    picture = models.FileField(upload_to='pictures')

    user = models.OneToOneField(User)

    @property
    def associated_social_network_accounts(self):
        return SocialAccount.objects.filter(
            user=self.user
        )

from .signals import *  # noqa

