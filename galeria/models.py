from django.db import models
from datetime import datetime
# Create your models here.
class photo(models.Model):
    tag_choices = [
        ('NEBULOSA', 'nebulosa'),
        ('ESTRELA', 'estrela'),
        ('GÁLAXIA', 'galaxia'),
        ('PLANETA', 'planeta'),
        ('CORPOS CELESTES','corpos celestes')
    ]
    name = models.CharField(max_length=100, null=False, blank=False)
    subtitle = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(null=False, blank=False) 
    image = models.ImageField(upload_to="images/%Y/%m/%d/", blank=True)
    tag = models.CharField(max_length=100, choices=tag_choices, default='')
    published = models.BooleanField(default=False)
    publish_date = models.DateTimeField(default=datetime.now(), blank=False)

    def __str__(self) -> str:
        return self.name