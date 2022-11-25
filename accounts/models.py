from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser
from app.utils import image_resize

class User (AbstractUser):
    is_author= models.BooleanField(default=False)
    
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    fullname = models.CharField(max_length=50)
    slug = models.CharField(max_length=50, editable=False)
    phone = models.CharField(max_length=15, default="")
    address = models.TextField(default="")
    picture = models.ImageField(upload_to='uploads/', blank=True, null=True)
    
    
    def __str__(self):
        return self.fullname
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.fullname)
        image_resize(self.picture, 200, 200)
        super(Author, self).save(*args, **kwargs)
        
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000/' + self.image.url