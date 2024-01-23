from django.db import models
from django.contrib.auth.models import User

class Subscriber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscribe = models.BooleanField(default=True)

    def __str__(self):
        return self.name + ' - ' + str(self.subscribe)
