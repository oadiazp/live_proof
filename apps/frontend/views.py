from django.urls import reverse
from django.views.generic import RedirectView, TemplateView

from apps.api.models import Profile


class LoginGatewayView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return reverse('profile')
        else:
            return reverse('account_login')


class ProfileView(TemplateView):
    template_name = 'frontend/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.filter(
            user__username=self.request.user.username
        ).first()

        return context


