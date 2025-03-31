from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.model):
    """
    This model extends the default Django User model to include additional fields.
    The user field is a OneToOneField that links to the User model for that specific user.
    Username, Fname, Lname and email are inherited from the User model.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    #profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    social_media_links = models.JSONField(blank=True, null=True)    # Store social media links as JSON

    def __str__(self):
        return str(self.user)