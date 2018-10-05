from django.db import models

class photos(models.Model):
        title = models.CharField(max_length=0)
        description = models.CharField(max_length=50,choices=CATEGORY_CHOICES)                     
        thumbnail = models.ImageField
        #(upload_to = 'uploaded_images/').
