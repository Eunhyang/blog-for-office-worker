from django.db import models
from django.utils import timezone

# Create your models here.
class HashTag(models.Model):
    name = models.CharField(max_length = 50)
    def __str__(self):
        return self.name

class Article(models.Model):
    DEVELOPMENT = 'dv'
    PERSONAL = 'ps'
    CATEGORY_CHOICES = (
        (DEVELOPMENT, 'development'),
        (PERSONAL, 'personal'),
    )
    title = models.CharField(max_length = 20)
    sub_title = models.CharField(max_length = 50)
    content = models.TextField()
    category = models.CharField(
        max_length = 2,
        choices = CATEGORY_CHOICES,
        default = DEVELOPMENT,
    )

    hashtag = models.ManyToManyField(HashTag)
    created_date = models.DateTimeField(default=timezone.now)

    def approved_comments(self):
        return self.article_comments.filter(approved_comment=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(
    Article,
    related_name = "article_comments",
    on_delete = models.CASCADE
    )
    username = models.CharField(max_length = 50)
    comment = models.CharField(max_length = 200)
    approved_comment = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)

    # def approve(self):
    # self.approved_comment = True
    # self.save()

    def __str__(self):
        return "{} 댓글: {}".format(self.article.title, self.comment)
