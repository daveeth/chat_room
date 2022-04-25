from django.db import models as m

# Create your models here.
class Room(m.Model):
    #host
    #topic
    name = m.CharField(max_length=60)
    description = m.TextField()
    #participants
    created_on = m.DateTimeField(auto_now_add=True)
    updated_on = m.DateTimeField(auto_now=True)

