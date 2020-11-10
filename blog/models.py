from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Post {self.title}'

    '''
        It is used to redirect browser to a specific url after an entity of model is created. Besides,
        it is good for DRY.
    '''
    def get_absolute_url(self):
        return reverse('blog-post', kwargs={'pk': self.pk})
