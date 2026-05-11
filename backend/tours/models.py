from django.db import models

class Tour(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='tours/')
    duration = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    experience_points = models.IntegerField()
    route = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class TourRoute(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='routes')
    order = models.IntegerField()
    location = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.tour.name} - {self.location}"
