import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Question

class QUestionModelTests(TestCase):
    def test_wpr(self):
        """ ...... """
        time = timezone.now() + datetime.timedelta(days = 30)

        future_question = Question(pub_date = time)

        self.assertIs(future_question.wpr(),False)

    def test_wpr_old_que(self):
        """
        
        """
        time = timezone.now() - datetime.timedelta(days=1,seconds=1)

        old_que = Question(pub_date =time)
        self.assertIs(old_que.wpr(),False)

    def test_wpr_recent_que(self):
        """
        """
        time = timezone.now() - datetime.timedelta(hours = 23,minutes=59,seconds=59)

        recent_que = Question(pub_date = time)
        self.assertIs(recent_que.wpr(),True)