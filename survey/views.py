from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

from survey.models import Question 

def main(request):    
    question = Question.objects.all()
    return render_to_response("survey.html", dict(question=question, user=request.user))        

def post(request, pk):
    return 1
    


def statistics(request):
    return 1