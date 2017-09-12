from django.contrib import admin

from .models import Insurance, LiveProof, Destination, Profile


class LiveProofInline(admin.TabularInline):
    model = LiveProof
    fields = ('proofed',)


@admin.register(Insurance)
class InstanceAdmin(admin.ModelAdmin):
    list_display = ('name', 'enabled',)
    inlines = (LiveProofInline,)


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'insurance', 'channel',)


admin.site.register(Profile)
