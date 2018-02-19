import datetime
from django.test import TestCase
from django.utils import timezone
from django.test import TestCase
from .models import Question
# Create your tests here.
class QuestionMehodTests(TestCase):
    def test_waspublished_recently_with_future_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        :return:
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(),False)
