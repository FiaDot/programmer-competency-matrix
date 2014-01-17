from django.contrib import admin
from survey.models import Question


class QustionAdmin(admin.ModelAdmin):
    list_display = ('seq', 'body', 'answer1', 'answer2', 'answer3', 'answer4') 
   
              
admin.site.register(Question, QustionAdmin)
