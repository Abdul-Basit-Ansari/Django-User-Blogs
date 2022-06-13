from distutils.command.upload import upload
import email
from email.policy import default
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.


class Blog(models.Model):
	sno = models.AutoField(primary_key=True)
	title = models.CharField(max_length=30,error_messages={'required':'Enter First Name First'})
	writter = models.CharField(max_length=50)
	slug=models.CharField(max_length=130)
	time = models.DateTimeField(auto_now_add=True)
	content = models.TextField()
	# img = models.ImageField()

	def __str__(self):
		return self.title

class Blogcomment(models.Model):

	sno = models.AutoField(primary_key=True)
	comment = models.TextField()
	user = models.ForeignKey(User , on_delete=models.CASCADE)
	blog = models.ForeignKey(Blog , on_delete=models.CASCADE)
	parent = models.ForeignKey('self', on_delete=models.CASCADE , null=True)
	time = models.DateTimeField(default=now)

	# img = models.ImageField()

	def __str__(self):
		return self.comment[0:13] + "..." + "by" + " " + self.user.username

