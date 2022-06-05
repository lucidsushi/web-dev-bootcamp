from statistics import mode
from string import ascii_uppercase

from django.db import models


# Create your models here.
# Django likes fat models and thin views?
class Room(models.Model):
    code = models.CharField(max_length=8, default="", unique=True)
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_slip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)


def generate_unique_code():
    '''
    Generate random code using a certain length in A-Z and check against existing codes.
    --------------------------------------------------
    # Returns the total number of entries in the database.
    Entry.objects.count()

    # Returns the number of entries whose headline contains 'Lennon'
    Entry.objects.filter(headline__contains='Lennon').count()
    '''
    length = 6
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Room.objects.filter(code=code).count() == 0:
            return code