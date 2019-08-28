from django.db import models

# Create your models here.

class ThingToDo(models.Model):
    """Define items for the list"""
    activity_text = models.CharField(max_length=500, default="", unique=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Things to do"

    def __str__(self):
        return self.activity_text