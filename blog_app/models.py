from django.db import models

# Create your models here.
# snake and passcall case in python

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_at = models.DateTimeField(null=True,blank=True)
    author = models.ForeignKey("auth.user", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    