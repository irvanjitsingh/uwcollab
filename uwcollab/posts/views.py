from rest_framework.views import APIView
from rest_framework.response import Response
import forms
from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils import simplejson as json
from models import Question
from chat import views
from chat.models import ChatRoom
from operator import attrgetter


class HomeView(APIView):
    template = 'home.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        questions = sorted(Question.objects.all(), key=attrgetter('id'), reverse=True)
        context = RequestContext(request, {'first_name': user.username, 'questions': questions})
        return render_to_response(self.template, context_instance=context)

    def post(self, request, *args, **kwargs):
        form = forms.PostForm(request.POST)
        try:
            if(form.is_valid()):
                title = request.POST.get('title', '')
                question = Question(user=request.user, title=request.POST.get('title', ''), content=request.POST.get('content', ''))
                question.save()
            questions = sorted(Question.objects.all(), key=attrgetter('id'), reverse=True)
            views.create(title)
            context = RequestContext(request, {'first_name': request.user.username, 'questions': questions})
            return render_to_response(self.template, context_instance=context)

        except ValidationError as v:
            return HttpResponseBadRequest(json.dumps(v.mesage_dict))
        except Exception as e:
            return HttpResponseBadRequest(json.dumps({'error': e.message}))


class PostView(APIView):
    template = 'post.html'

    def get(self, request, *args, **kwargs):
        try:
            question = Question.objects.get(id=int(kwargs['post_id']))
            chat_room = ChatRoom.objects.get(name=question.title)
            context = RequestContext(request, {'first_name': request.user.username, 'question': question, 'room': get_object_or_404(ChatRoom, slug=chat_room.slug)})
            return render_to_response(self.template, context_instance=context)
        except Question.DoesNotExist as e:
            return Response(400, e.message)

