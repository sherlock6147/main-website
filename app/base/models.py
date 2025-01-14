from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class WhiteListedPeople(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.user.first_name + self.user.last_name