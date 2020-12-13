from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	img = models.ImageField(default='default.jpg', upload_to='user_images')

	def __str__(self):
		return f'Профиль{self.user.username}'

	def save(self, *args, **kwargs):
		super().save()
