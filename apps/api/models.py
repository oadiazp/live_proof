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

    channels = models.ManyToManyField('Channel', through='Destination')


CHANNEL_TYPE = NamedChoices((
    ('EMAIL', _('E-mail')),
))


class Channel(TimeStampedModel, StringOverridedModel):
    name = models.CharField(max_length=200)
    type = models.CharField(
        max_length=CHANNEL_TYPE.max_length,
        choices=CHANNEL_TYPE
    )


class Destination(TimeStampedModel, StringOverridedModel):
    name = models.CharField(max_length=200)

    insurance = models.ForeignKey(Insurance)
    channel = models.ForeignKey(Channel)


class LiveProof(TimeStampedModel):
    proofed = models.BooleanField(default=False)

    insurance = models.ForeignKey(Insurance)
