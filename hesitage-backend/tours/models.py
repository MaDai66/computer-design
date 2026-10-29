from django.db import models

class Tour(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.CharField(max_length=500, blank=True, null=True)
    image_base64 = models.TextField(blank=True, null=True)
    gallery_base64 = models.JSONField(default=list)
    gallery_images = models.JSONField(default=list)
    duration = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    experience_points = models.IntegerField(default=0)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    rating_count = models.IntegerField(default=0)
    review_count = models.IntegerField(default=0)
    sales_count = models.IntegerField(default=0)
    difficulty = models.CharField(max_length=50, default="中等")
    tags = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class TourDay(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='days')
    day_number = models.IntegerField()
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.tour.name} - Day {self.day_number}"

class TimeSlot(models.Model):
    day = models.ForeignKey(TourDay, on_delete=models.CASCADE, related_name='time_slots')
    time = models.CharField(max_length=50)
    activity = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.time} - {self.activity}"

class HeritageHighlight(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='highlights')
    icon = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.title

class CostInfo(models.Model):
    tour = models.OneToOneField(Tour, on_delete=models.CASCADE, related_name='cost_info')
    includes = models.JSONField(default=list)
    excludes = models.JSONField(default=list)
    booking_notes = models.JSONField(default=list)
    
    def __str__(self):
        return f"Cost info for {self.tour.name}"

class TourReview(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='reviews')
    user_name = models.CharField(max_length=100)
    avatar = models.URLField(blank=True, null=True)
    rating = models.IntegerField()
    content = models.TextField()
    images = models.JSONField(default=list)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"Review by {self.user_name} for {self.tour.name}"
