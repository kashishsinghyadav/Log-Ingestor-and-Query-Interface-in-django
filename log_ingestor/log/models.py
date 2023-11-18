from django.db import models
class Logl(models.Model):
    level = models.CharField(max_length=50)
    message = models.TextField()
    resourceId = models.CharField(max_length=50)
    timestamp = models.DateTimeField()
    traceId = models.CharField(max_length=50)
    spanId = models.CharField(max_length=50)
    commit = models.CharField(max_length=50)
    parentResourceId = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.level} - {self.message}"

# Create your models here.
