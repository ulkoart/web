from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def new(self):
        return super(QuestionManager, self).get_queryset().order_by('-added_at')

    def popular(self):
        return super(QuestionManager, self).get_queryset().order_by('-likes')


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions', blank=True, null=True)
    likes = models.ManyToManyField(User, blank=True)
    objects = QuestionManager()

    def get_url(self):
    	return "/question/{0}/".format(self.id) 

    def __str__(self):
        return self.title


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.text
