from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    date_created = models.DateTimeField('Date Published')
    date_updated = models.DateTimeField('Date Updated')
    content = models.TextField()
    is_active = models.BooleanField(default=True)



class Comment(models.Model):
    date_created = models.DateTimeField('Date Published')
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name = 'choices')
