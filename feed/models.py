from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    DEVELOPMENT = 'dv'
    PERSONAL = 'ps'
    CATEGORY_CHOICES = (
        (DEVELOPMENT, 'development'),
        (PERSONAL, 'personal'),
    )
    title = models.CharField(max_length = 20)
    content = models.TextField()
    category = models.CharField(
        max_length = 2,
        choices = CATEGORY_CHOICES,
        default = DEVELOPMENT,
    )
    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article)
    username = models.CharField(max_length = 50)
    comment = models.CharField(max_length = 200)
    def __str__(self):
        return "{} 댓글: {}".format(self.article.title, self.comment)

class HashTag(models.Model):
    name = models.CharField(max_length = 50)
