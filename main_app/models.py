from django.db import models
from django.urls import reverse

# Create your models here.
class Motorcycle(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField()

    def __str__(self):
        return self.name
    
    # Needed to redirect after you CREATE the cat on the form
    def get_absolute_url(self):
        return reverse('detail', kwargs={'motorcycle_id': self.id}) #kwags is optional, but we are requiring an id, so we need to use it