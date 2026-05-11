from django.db import models

class Homestay(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='homestay/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    rooms = models.IntegerField()
    amenities = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class HomestayExperience(models.Model):
    homestay = models.ForeignKey(Homestay, on_delete=models.CASCADE, related_name='experiences')
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
