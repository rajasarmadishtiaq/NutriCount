from django.db import models
from account.models import Profile
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


class Network(models.Model):
    mentee = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='mentee')
    mentor = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='mentor')


class NetworkSearch(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def get_mentors(self):
        return Network.objects.filter(mentee=self.user)

    def get_mentees(self):
        return Network.objects.filter(mentor=self.user)
