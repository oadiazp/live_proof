from django.contrib import admin

from .models import Insurance, LiveProof, Destination, Profile


class LiveProofInline(admin.TabularInline):
    model = LiveProof
    fields = ('proofed',)


class DestinationInline(admin.TabularInline):
    model = Destination
    fields = ('name', 'channel', 'file',)


@admin.register(Insurance)
class InsuranceAdmin(admin.ModelAdmin):
    list_display = ('name', 'enabled',)
    inlines = (DestinationInline, LiveProofInline,)


admin.site.register(Profile)
