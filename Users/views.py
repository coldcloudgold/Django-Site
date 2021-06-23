from django.urls import reverse_lazy
from allauth.account.views import PasswordChangeView as allauth_PasswordChangeView
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required


class PasswordChangeView(allauth_PasswordChangeView):
    success_url = reverse_lazy("custom_change_password_done")


password_change = login_required(PasswordChangeView.as_view())


class PasswordChangeDoneView(TemplateView):
    template_name = "account/password_reset_from_key_done.html"


password_change_done = PasswordChangeDoneView.as_view()
