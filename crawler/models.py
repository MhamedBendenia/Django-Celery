from django.db import models

class Reviews(models.Model):
    userName = models.TextField()
    userImage = models.TextField()
    content = models.TextField()
    score = models.IntegerField()
    thumbsUpCount = models.IntegerField()
    reviewCreatedVersion = models.TextField()
    at = models.DateTimeField()
    replyContent = models.TextField(null=True)
    repliedAt = models.DateTimeField(null=True)
    reviewId = models.TextField(primary_key=True)
