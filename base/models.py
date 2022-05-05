from django.db import models as m
from django.contrib.auth.models import User

# Create your models here.

class Topic(m.Model):
	name = m.CharField(max_length=200)

	def __str__(self):
		return self.name[0:50]

class Room(m.Model):
    host = m.ForeignKey(User, on_delete=m.SET_NULL, null=True)
    topic = m.ForeignKey(Topic, on_delete=m.SET_NULL, null=True)
    name = m.CharField(max_length=60)
    description = m.TextField()
    #participants
    created_on = m.DateTimeField(auto_now_add=True)
    updated_on = m.DateTimeField(auto_now=True)

    def __str__(self):
    	return self.name

class Message(m.Model):
	user = m.ForeignKey(User, on_delete=m.CASCADE)
	room = m.ForeignKey(Room, on_delete=m.SET_NULL, null=True)
	body = m.TextField()
	created_on = m.DateTimeField(auto_now_add=True)
	updated_on = m.DateTimeField(auto_now=True)

	def __str__(self):
		return self.body[:60]