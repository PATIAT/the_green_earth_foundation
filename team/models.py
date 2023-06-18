from django.db import models


# Create your models here.
class TeamMember(models.Model):
    name = models.CharField(max_length=254, null=False, blank=False)
    age = models.PositiveIntegerField()
    biography = models.TextField()
    favorite_place = models.CharField(max_length=100, null=False, blank=False)
    passion = models.CharField(max_length=100, null=False, blank=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
