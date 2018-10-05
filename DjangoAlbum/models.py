from django.db import models

class photos(models.Model):
        title = models.CharField(max_length=200)
        description = models.CharField(max_length=500)                     
        thumbnail = models.ImageField(upload_to = 'uploaded_images/')
        #(upload_to = 'uploaded_images/').
