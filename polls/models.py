from django.db import models
import datetime
from django.utils import timezone
# Create your every model just here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date Published')
    # que_type = models.CharField(max_length = 10)#自定义的问题类型，限制为10个字符

    #即:def was_published_recently(self):  简记做wpr!!!
    def wpr(self):
        now = timezone.now()
        return now >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(
        Question
        ,on_delete=models.CASCADE
    )
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.choice_text
