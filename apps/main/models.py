from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=123)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField()
    subject = models.CharField(max_length=123, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
