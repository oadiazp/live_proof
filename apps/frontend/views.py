from django.urls import reverse
from django.views.generic import RedirectView, TemplateView


class LoginGatewayView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return reverse('profile')
        else:
            return reverse('account_login')


class ProfileView(TemplateView):
    template_name = 'frontend/profile.html'
