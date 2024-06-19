from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=212)
    description = models.TextField()
    is_done = models.BooleanField(default=False)
    crested_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title