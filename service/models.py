from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

from markdown import Markdown


class Service(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='Services'
    )

    # 标题
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created']


    def __str__(self):
        return self.title

    def get_md(self):
        md = Markdown(
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
            ]
        )
        md_body = md.convert(self.content)
        return md_body, md.toc