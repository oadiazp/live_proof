from django.contrib import admin

from .models import Insurance, LiveProof, Channel, Destination, Profile


class LiveProofInline(admin.TabularInline):
    model = LiveProof
    fields = ('proofed', 'created',)


@admin.register(Insurance)
class InstanceAdmin(admin.ModelAdmin):
    list_display = ('name', 'enabled',)
    inlines = (LiveProofInline,)


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ('name', 'type',)


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'insurance', 'channel',)

admin.site.register(Profile)
