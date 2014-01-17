from django.db import models


class Question(models.Model):
    seq = models.AutoField(primary_key=True)
    body = models.CharField(max_length=100)
    answer1 = models.TextField()
    answer2 = models.TextField()
    answer3 = models.TextField()
    answer4 = models.TextField()
    
    def __str__(self):
        return self.body



class User(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()    
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name



class Answer(models.Model):
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    answer = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s : %s : %d" % (self.user, self.question, self.answer)   
