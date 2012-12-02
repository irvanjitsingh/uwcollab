# Create your views here.

# Create your views here.
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.views.generic.base import View
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.utils import simplejson as json
from django.db.transaction import commit_on_success
from django.views.generic.edit import FormView
from forms import RegistrationForm


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')


def home(request):
    template = 'home.html'
    user = request.user
    context = {'first_name': user.username}
    return render_to_response(template, context)


class RegistrationView(FormView):
    """
    Form view to handle registration
    """
    form_class = RegistrationForm
    success_url = "/"

    @commit_on_success
    def form_valid(self, form):
        form.save()

        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])

        # tasks.send_template_email.delay(settings.EMAIL_HOST_USER, [form.cleaned_data['email']],
        #                             'registration/activation_email_subject.txt', {},
        #                             'registration/activation_email.txt', {'user': user})
        login(self.request, user)

        return super(RegistrationView, self).form_valid(form)


class LandingView(View):
    template = 'login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('home'))
        context = {}
        return render(request, self.template, context)

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponseRedirect(reverse('login'))
