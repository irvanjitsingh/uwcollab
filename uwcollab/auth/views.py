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


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')


def home(request):
    template = 'home.html'
    user = request.user
    context = {'first_name': user.username}
    return render_to_response(template, context)


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
