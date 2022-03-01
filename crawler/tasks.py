from hello_again.celery import app
from django.conf import settings
from celery.schedules import crontab
from google_play_scraper import reviews_all
from .models import Reviews

@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):

    # Executes every one hour
    sender.add_periodic_task(
        crontab(hour='*/1'),
        crawl.s(settings.APP_ID),
        name='Crawl every one hour'
    )

# Saving reviews in the database
@app.task
def save_review(review):
    r = Reviews(**review)
    r.save()

# Fetching all reviews
@app.task
def crawl(app_id = settings.APP_ID):
    result = reviews_all(
        app_id,
        country='at',
    ) 
    for review in result:
        save_review.delay(review)
    
    return result