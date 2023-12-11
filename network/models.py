from django.db import models
from account.models import Profile
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

REQUEST_STATUS = [
    (0, 'Pending'),
    (1, 'Accepted')
]


class Network(models.Model):
    mentee = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='mentee')
    mentor = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='mentor')
    request = models.IntegerField(choices=REQUEST_STATUS, default=0)


class NetworkSearch(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def get_mentors(self, request=None):
        return Network.objects.filter(mentee=self.user, request=request)

    def get_mentees(self, request=None):
        return Network.objects.filter(mentor=self.user, request=request)
