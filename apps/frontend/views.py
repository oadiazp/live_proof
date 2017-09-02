from django.urls import reverse
from django.views.generic import RedirectView


class LoginGatewayView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            pass
        else:
            return reverse('account_login')
