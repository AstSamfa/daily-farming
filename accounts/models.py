from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(default='default_profile_pic.jpg', upload_to='perfil_pics')

    class Meta:
        db_table = 'perfiles'


