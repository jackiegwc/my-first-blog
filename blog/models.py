from django.db import models
from django.utils import timezone

class Post(models.Model):   #defines our model (object), models.Model --> post is a Django Model
	author = models.ForeignKey('auth.User')    #link to another model 
	title = models.CharField(max_length=200)  #define text w/ a limited num of chars
	text = models.TextField()                  #long text w/out a lim
	created_date = models.DateTimeField(       #datetimefield is a date and time
		default=timezone.now)
	published_date= models.DateTimeField(
		blank=True, null=True)

	def publish(self):                        #this is a function/method
		self.published_date=timezone.now()     #method belongs to the class
		self.save()

	def __str__(self):
		return self.title