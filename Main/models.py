from django.db import models
from django.contrib.auth.models import User
from tinymce import models as tinymce_models


# Create your models here.

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, editable=True)
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('publication date', auto_now_add=True)
    article = tinymce_models.HTMLField()
    image = models.ImageField(upload_to='articles', blank=True, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=250)
    pub_date = models.DateTimeField('publication date', auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment