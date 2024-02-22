from django.db import models
# from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     pass

class Food(models.Model):
    fdc_id = models.IntegerField()
    description = models.CharField(max_length=500)

    def getTHEFOOD(self):
        return {
            "name": self.description
        }
