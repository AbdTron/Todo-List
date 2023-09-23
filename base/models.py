from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    
    "What happens when the user is deleted --> delete all data related to the user."
    "ForeignKey is one to many relation"
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    
    "Auto populate this feild so we dont have to do it everytime"
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        
        "Arrange items so that the comeplete items are at the bottom"
        ordering = ['complete']

