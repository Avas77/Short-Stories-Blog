from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.urls import reverse

class Writing(models.Model):
	title = models.CharField(max_length=200)
	short_description = models.TextField(blank = True)
	description = models.TextField()
	categories = models.CharField(max_length=200)
	
	write_date = models.DateTimeField(default = datetime.now, blank = True)
	is_mvp = models.BooleanField(default=False)
	author=models.ForeignKey(User,on_delete=models.CASCADE)
	
	def __str__(self):
		return self.title  

	def get_absolute_url(self):
		return reverse('writing-detail',kwargs={'pk':self.pk})  
# Create your models here.
