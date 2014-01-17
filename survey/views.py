from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import render
from survey.models import Question 

def main(request):    
    #question = Question.objects.all()
    #return render_to_response("survey.html", dict(question=question))

    question = Question.objects.all()
    context = {'question_list': question}
    return render(request, 'survey.html', context)

        

def submit(request):
    question = Question.objects.all()
    context = {'question_list': question}
    return render(request, 'survey.html', context)


def statistics(request):
    return 1