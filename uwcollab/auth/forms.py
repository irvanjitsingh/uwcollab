from django import forms

from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User


class RegistrationForm(forms.Form):
    """
    Form for registering a new user account.

    Validates that the requested username is not already in use, and
    requires the password to be entered twice to catch typos.
    """
    #TODO: change static and media to be populated from settings
    APP_RESERVED_URLS = ['app', 'api', 'static', 'media']

    username = forms.RegexField(regex=r'^[\w]+$',
                                max_length=30,
                                widget=forms.TextInput(),
                                label=_("Custom URL"),
                                error_messages={'invalid': _("This value may contain only letters, numbers and \-\_ characters.")})
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(maxlength=75)),
                             label=_("E-mail"))
    password = forms.CharField(widget=forms.PasswordInput(render_value=False),
                                label=_("Password"))

    def clean_email(self):
        """
        Validate that the username is alphanumeric and is not already
        in use.
        """
        existing = User.objects.filter(email__iexact=self.cleaned_data['email'])
        if existing.exists():
            raise forms.ValidationError(_("A user with that email already exists."))
        else:
            return self.cleaned_data['email']

    def clean_username(self):
        """
        Validate that the username is alphanumeric and is not already
        in use.
        """
        existing = User.objects.filter(username__iexact=self.cleaned_data['username'])
        if existing.exists():
            raise forms.ValidationError(_("A user with that url already exists."))
        elif self.cleaned_data['username'] in self.APP_RESERVED_URLS:
            raise forms.ValidationError(_("This url is already taken by the wishmark appplication."))
        else:
            return self.cleaned_data['username']

    def save(self):
        user = User.objects.create_user(username=self.cleaned_data['username'],
                                            email=self.cleaned_data['email'],
                                            password=self.cleaned_data['password'])

        return user