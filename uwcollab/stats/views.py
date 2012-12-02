from posts.models import Question
from django.shortcuts import render, render_to_response
from django.template import RequestContext
import stats.analyzer as f, pdb

def stats(request):

    # Frequency analysis
    text = ''
    for body in Question.objects.all():
        string = body.content + ' '
        text += string
    freq = f.analyze(text, 10)

    # Question views
    titles = []
    counter = 0
    for name in Question.objects.all():
        counter += 1
        if counter < 3:
            titles.append(name.title)

    views = titles
    context = RequestContext(request, {'frequency': freq, 'views': views})
    return render_to_response('stats.html', context_instance=context)

        