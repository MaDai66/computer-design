from django.db import models
from users.models import User

class CommunityPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='community/')
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class TravelNote(models.Model):
    post = models.OneToOneField(CommunityPost, on_delete=models.CASCADE, related_name='travel_note')
    location = models.CharField(max_length=255)
    duration = models.CharField(max_length=100)
    tags = models.CharField(max_length=255)
    
    def __str__(self):
        return f"Travel Note: {self.post.title}"
