from django import forms
from django.contrib.auth import forms as auth_forms
from django.utils.translation import gettext_lazy as _

from e_shop.e_shop_base.models import Profile, UserModel


class RegisterUserForm(auth_forms.UserCreationForm):

    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Repeat password!!!"),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.help_text = _("It works")

    def save(self, commit=True):
        user = super().save(commit)

        profile = Profile(email=self.cleaned_data["email"],
                          user=user, )
        if commit:
            profile.save()

        return user

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ("email",)
