from django.db import models

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
    image = models.CharField(max_length=100, null=False, blank=False)
    tag = models.CharField(max_length=100, choices=tag_choices, default='')

    def __str__(self) -> str:
        return f'Photography {self.name}'