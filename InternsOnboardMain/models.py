from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class internshipPost(models.Model):
<<<<<<< HEAD
    company_name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.company_name
=======
    Uploader_info = models.CharField(max_length=100, editable=False, null = True)
    company_name = models.CharField(max_length=100,blank=False)
    discription = models.TextField(max_length=1000,blank=False)
    owner = models.ForeignKey(User, related_name="coordinatorName", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name


>>>>>>> master
