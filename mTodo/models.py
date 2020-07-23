from django.db import models


# Create your models here.

# Create your views here.

class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title
