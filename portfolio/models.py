from django.db import models
from django.core.exceptions import ValidationError
import os
import uuid
import datetime
from django.conf import settings
from django.contrib.auth.models import User


# Function to generate unique file names
def getfilename(request, filename):
    now_time = datetime.datetime.now().strftime("%Y:%m:%d:%H:%M:%S")
    unique_id = uuid.uuid4().hex
    filename = f"{now_time}_{unique_id}_{filename}"
    return os.path.join('uploads/', filename)


def getfilename_icon(request, filename):
    now_time = datetime.datetime.now().strftime("%Y:%m:%d:%H:%M:%S")
    unique_id = uuid.uuid4().hex
    filename = f"{now_time}_{unique_id}_{filename}"
    return os.path.join('uploads/icon/', filename)



# File type validation for images
def validate_file_type(value):
    valid_extensions = ['.jpg', '.jpeg', '.png']
    ext = os.path.splitext(value.name)[1]
    if ext.lower() not in valid_extensions:
        raise ValidationError('Unsupported file extension. Allowed extensions: .jpg, .jpeg, .png')


# Profile model (with user association)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE ,null=True)  # Associate Profile with Django User model
    name = models.CharField(max_length=50, null=False, blank=False)
    role = models.CharField(max_length=50, null=False, blank=False)
    Dp = models.ImageField(upload_to=getfilename, null=True, blank=True, validators=[validate_file_type])
    about = models.TextField(max_length=500, null=False, blank=False)
    create_at = models.DateTimeField(auto_now_add=True)
    linkedin = models.URLField(max_length=200, null=True, blank=True)
    index_linkedin = models.CharField(max_length=200, null=False, blank=False, default="dk")
    email = models.EmailField(max_length=200, null=False, blank=False)
    index_email = models.EmailField(max_length=200, null=False, blank=False, default="example@example.com")
    git = models.URLField(max_length=200, null=False, blank=False, default="https://github.com/example")
    index_git = models.URLField(max_length=120, null=False, blank=False, default="https://github.com/example")
    phone = models.CharField(max_length=200, null=False, blank=False, default="+91 1234567890")
    index_phone = models.CharField(max_length=200, null=False, blank=False, default="phone")

    def __str__(self):
        return self.name


# Work model
class Work(models.Model):
    title = models.CharField(max_length=150, null=False, blank=False)
    icon = models.ImageField(upload_to=getfilename_icon, null=True, blank=True, validators=[validate_file_type])
    dec = models.CharField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.title


# Education model
class Education(models.Model):
    title = models.CharField(max_length=150, null=False, blank=False)
    duration = models.CharField(max_length=150, null=False, blank=False)
    percentage = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return self.title


# Skills model
class Skills(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    icon = models.ImageField(upload_to=getfilename_icon, null=True, blank=True, validators=[validate_file_type])

    def __str__(self):
        return self.name


# Certificate model
class Certificate(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    id_url = models.URLField(max_length=200, null=False, default="https://www.linkedin.com/in/example/")
    img = models.ImageField(upload_to=getfilename, null=True, blank=True, validators=[validate_file_type])

    def __str__(self):
        return self.name


# Project model
class Project(models.Model):
    title = models.CharField(max_length=150, null=False, blank=False)
    type = models.CharField(max_length=100, null=False, blank=False)
    url = models.URLField(max_length=200, null=False, blank=False)
    img = models.ImageField(upload_to=getfilename, null=True, blank=True, validators=[validate_file_type])

    def __str__(self):
        return self.title


# Add custom permissions if necessary for access control
class Meta:
    permissions = [
        ("can_view_profile", "Can view profile"),
        ("can_edit_profile", "Can edit profile"),
    ]
