from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

User._meta.get_field('email')._unique = True

class Project(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(default=f"""\
# {title}
{author}
{date}

## Introduction
""")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'pk':self.pk})
