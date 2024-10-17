from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
class photo(models.Model):
    tag_choices = [
        ('NEBULOSA', 'nebulosa'),
        ('ESTRELA', 'estrela'),
        ('GÁLAXIA', 'galaxia'),
        ('PLANETA', 'planeta'),
        ('Satélites','satelites')
    ]
    name = models.CharField(max_length=100, null=False, blank=False)
    subtitle = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(null=False, blank=False) 
    image = models.ImageField(upload_to="images/%Y/%m/%d/", blank=True)
    tag = models.CharField(max_length=100, choices=tag_choices, default='')
    published = models.BooleanField(default=True)
    publish_date = models.DateTimeField(default=datetime.now(), blank=False)
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='user'
        )

    def __str__(self) -> str:
        return self.name