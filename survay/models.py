from django.db import models


class Survay(models.Model):
    question = models.TextField()
    answer1 = models.TextField()
    answer2 = models.TextField()
    answer3 = models.TextField()
    answer4 = models.TextField()
    
    def __str__(self):
        return "%s" % (self.question[:40])
 


class User(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()    
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name



class Answer(models.Model):
    user = models.ForeignKey(User)
    survay = models.ForeignKey(Survay)
    answer = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s : %s : %d" % (self.user, self.survay, self.answer)   
        