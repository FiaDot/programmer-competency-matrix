from django.contrib import admin
from survey.models import Question
from survey.models import User
from survey.models import Answer 


class QustionAdmin(admin.ModelAdmin):
    list_display = ('seq', 'body', 'answer1', 'answer2', 'answer3', 'answer4') 
   
              
admin.site.register(Question, QustionAdmin)



class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    
admin.site.register(User, UserAdmin)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'answer', 'created')

admin.site.register(Answer, AnswerAdmin)   