from django.db import models

class Heritage(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='heritage/')
    category = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class HeritageExperience(models.Model):
    heritage = models.ForeignKey(Heritage, on_delete=models.CASCADE, related_name='experiences')
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=100)
    available_slots = models.IntegerField()
    
    def __str__(self):
        return self.title
