from django.test import TestCase
from .models import Reviews
from hello_again.celery import app
from .tasks import crawl


class ReviewsTestCase(TestCase):

    def test_if_can_scrawl(self):
        results = crawl.delay("com.color.number.sanbox.pixel.art").get(timeout=10)
        self.assertNotEqual(len(results), 0)

