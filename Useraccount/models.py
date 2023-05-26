from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models


import uuid



class User(AbstractUser):
    email = models.EmailField(('email address'), unique=True)
    fullname = models.CharField(max_length=100)
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []

    
