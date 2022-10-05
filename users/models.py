from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from PIL import Image    #to reduce pixels of img

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default= 'default.jpg', upload_to='profile-pics')

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img=Image.open(self.image.path)

        if img.height>300 or img.width>300:
            outpur_size = (300,300)             #damn it should be output_size (L take)
            img.thumbnail(outpur_size)          #             ^^^^^
            img.save(self.image.path)
        