from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.db.models import Max

from survey.models import Question
from survey.models import User
from survey.models import Answer 

from survey.forms import UserForm

import logging

logger = logging.getLogger(__name__)


def main(request):    
    #question = Question.objects.all()
    #return render_to_response("survey.html", dict(question=question))

    question = Question.objects.all()
#    context = {'question_list': question}
#    return render(request, 'survey.html', context)

    d = dict(question_list=question, form=UserForm())
    d.update(csrf(request))
    
    return render_to_response("survey.html", d)      




def submit(request):
    logger.info(request.POST)
    p = request.POST
    
    # 유져 정보 저장
    user = User(email=p["email"], name=p["name"], exp=p["exp"])        
    user.save();
    
    
    # 문항 최대 번호 검색
    max_seq_record = Question.objects.all().aggregate(Max('seq'))
    max_seq = int(max_seq_record['seq__max']) + 1
    
    
    # 점수 계산, 답변 저장
    score = 0

    for i in range(1, max_seq):        
        question = Question.objects.get(seq=i)           
        
        value = '%s' % i        
        score += int(p[value])
        logger.error(p[value])
        
        answer = Answer(user=user, question=question, answer=p[value])
        answer.save()
        
        
    d = dict(user=user, score=score)
    d.update(csrf(request))    
    return render_to_response("submit.html", d)


def user(request, pk):
    user = User.objects.get(pk=int(pk))
    
    answers = Answer.objects.get(user=user)
            
    d = dict(user=user, answers=answers)    
    return render_to_response("statistics.html", d)
    


def statistics(request):
    return 1